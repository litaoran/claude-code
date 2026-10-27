#!/usr/bin/env python3
"""Fetch current GPU rental prices from public provider APIs.

Writes two JSON files for the GPU Rental Prices dashboard:

  offers.json   one row per priced offer (instance x pricing tier), all providers
  history.json  per-run summary rows (gpu x pricing), appended to the
                previous history passed with --history and trimmed to --keep-days

Sources (no API keys needed):
  Vast.ai     marketplace offers        console.vast.ai/api/v0/bundles/
  RunPod      per-GPU list prices       api.runpod.io/graphql
  DataCrunch  instance types            api.datacrunch.io/v1/instance-types
  Azure       retail VM prices          prices.azure.com/api/retail/prices
  AWS         EC2 on-demand and spot    b0.p.awsstatic.com, website.spot.ec2.aws.a2z.com

Usage:
  python3 fetch_gpu_prices.py --out-dir DIR [--history PREV_HISTORY.json] [--keep-days 14]
"""

import argparse
import concurrent.futures as cf
import datetime as dt
import gzip
import json
import os
import re
import statistics
import sys
import urllib.parse
import urllib.request

UA = "gpu-rental-prices-dashboard/1.0"


def http(url, data=None, headers=None, timeout=60):
    hdrs = {"User-Agent": UA, "Accept-Encoding": "gzip"}
    hdrs.update(headers or {})
    req = urllib.request.Request(url, data=data, headers=hdrs)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        body = r.read()
        if r.headers.get("Content-Encoding") == "gzip" or body[:2] == b"\x1f\x8b":
            body = gzip.decompress(body)
        return body.decode("utf-8")


def http_json(url, payload=None, **kw):
    data = None
    headers = {}
    if payload is not None:
        data = json.dumps(payload).encode()
        headers["Content-Type"] = "application/json"
    return json.loads(http(url, data=data, headers=headers, **kw))


# --------------------------------------------------------------------------
# GPU name normalisation

SEGMENTS = {
    "Flagship datacenter": ["GB300", "B300", "GB200", "B200", "H200", "H200 NVL", "H100 SXM",
                            "H100 PCIe", "H100 NVL", "GH200", "MI325X", "MI300X"],
    "Datacenter": ["A100 80GB", "A100 40GB", "A800", "H800", "H20", "L40S", "L40", "A40", "A10",
                   "A10G", "A30", "A16", "L4", "T4", "V100", "P100"],
    "Workstation": ["RTX PRO 6000", "RTX PRO 5000", "RTX PRO 4500", "RTX PRO 4000",
                    "RTX 6000 Ada", "RTX 5000 Ada", "RTX 4000 Ada", "RTX 2000 Ada", "RTX A6000",
                    "RTX A5000", "RTX A4500", "RTX A4000", "RTX A2000", "Quadro RTX 8000"],
}
SEGMENT_OF = {g: s for s, gs in SEGMENTS.items() for g in gs}

RULES = [
    (r"GB300", "GB300"), (r"B300", "B300"), (r"GB200", "GB200"), (r"B200", "B200"),
    (r"GH200", "GH200"), (r"H200\s*NVL", "H200 NVL"), (r"H200", "H200"),
    (r"H100\s*NVL", "H100 NVL"), (r"H100.*PCI", "H100 PCIe"), (r"H100", "H100 SXM"),
    (r"H800", "H800"), (r"\bH20\b", "H20"), (r"MI325", "MI325X"), (r"MI300", "MI300X"),
    (r"A800", "A800"), (r"L40S", "L40S"), (r"\bL40\b", "L40"), (r"\bL4\b", "L4"),
    (r"\bA40\b", "A40"), (r"A10G", "A10G"), (r"\bA10\b", "A10"), (r"\bA30\b", "A30"),
    (r"\bA16\b", "A16"), (r"\bT4\b", "T4"), (r"V100", "V100"), (r"P100", "P100"),
    (r"RTX\s*PRO\s*6000", "RTX PRO 6000"), (r"RTX\s*PRO\s*5000", "RTX PRO 5000"),
    (r"RTX\s*PRO\s*4500", "RTX PRO 4500"), (r"RTX\s*PRO\s*4000", "RTX PRO 4000"),
    (r"6000.*ADA", "RTX 6000 Ada"), (r"5000.*ADA", "RTX 5000 Ada"),
    (r"4000.*ADA", "RTX 4000 Ada"), (r"2000.*ADA", "RTX 2000 Ada"), (r"A6000", "RTX A6000"),
    (r"A5000", "RTX A5000"), (r"A4500", "RTX A4500"), (r"A4000", "RTX A4000"),
    (r"A2000", "RTX A2000"), (r"RTX\s*8000", "Quadro RTX 8000"),
]


def norm_gpu(raw, vram_gb=None):
    s = raw.upper().replace("NVIDIA", " ").replace("GEFORCE", " ").replace("TESLA", " ")
    s = re.sub(r"\s+", " ", s).strip()
    if "A100" in s:
        return "A100 80GB" if (vram_gb or 80) >= 60 or "80G" in s else "A100 40GB"
    for pat, name in RULES:
        if re.search(pat, s):
            return name
    m = re.search(r"RTX\s?(\d{4})\s?(TI|SUPER|D|S)?\b", s)
    if m:
        suffix = {"TI": " Ti", "SUPER": " Super", "D": "D", "S": " S"}.get(m.group(2) or "", "")
        return f"RTX {m.group(1)}{suffix}"
    m = re.search(r"GTX\s?(\d{4})\s?(TI)?", s)
    if m:
        return f"GTX {m.group(1)}{' Ti' if m.group(2) else ''}"
    return raw.strip()


def segment(gpu):
    if gpu in SEGMENT_OF:
        return SEGMENT_OF[gpu]
    if gpu.startswith(("RTX ", "GTX ")):
        return "Consumer"
    return "Other"


def vendor(gpu):
    return "AMD" if gpu.startswith("MI") else "NVIDIA"


# --------------------------------------------------------------------------
# Geography

GEO_OF_COUNTRY = {}
for geo, codes in {
    "North America": "US CA MX",
    "South America": "BR AR CL CO PE UY",
    "Europe": "GB UK IE FR DE NL BE LU CH AT IT ES PT SE NO FI DK IS PL CZ SK HU RO BG GR "
              "LT LV EE SI HR RS UA MD BY TR",
    "Asia-Pacific": "JP KR CN TW HK SG MY TH VN ID PH IN AU NZ KZ",
    "Middle East": "AE SA QA IL BH OM KW JO",
    "Africa": "ZA NG KE EG MA",
}.items():
    for c in codes.split():
        GEO_OF_COUNTRY[c] = geo


def geo_of(country):
    return GEO_OF_COUNTRY.get((country or "").upper(), "Unspecified")


AWS_REGIONS = {
    "us-east-1": ("US East (N. Virginia)", "US"), "us-east-2": ("US East (Ohio)", "US"),
    "us-west-1": ("US West (N. California)", "US"), "us-west-2": ("US West (Oregon)", "US"),
    "ca-central-1": ("Canada (Central)", "CA"), "ca-west-1": ("Canada West (Calgary)", "CA"),
    "mx-central-1": ("Mexico (Central)", "MX"),
    "sa-east-1": ("South America (Sao Paulo)", "BR"),
    "eu-central-1": ("Europe (Frankfurt)", "DE"), "eu-central-2": ("Europe (Zurich)", "CH"),
    "eu-west-1": ("Europe (Ireland)", "IE"), "eu-west-2": ("Europe (London)", "GB"),
    "eu-west-3": ("Europe (Paris)", "FR"), "eu-north-1": ("Europe (Stockholm)", "SE"),
    "eu-south-1": ("Europe (Milan)", "IT"), "eu-south-2": ("Europe (Spain)", "ES"),
    "ap-northeast-1": ("Asia Pacific (Tokyo)", "JP"), "ap-northeast-2": ("Asia Pacific (Seoul)", "KR"),
    "ap-northeast-3": ("Asia Pacific (Osaka)", "JP"), "ap-southeast-1": ("Asia Pacific (Singapore)", "SG"),
    "ap-southeast-2": ("Asia Pacific (Sydney)", "AU"), "ap-southeast-3": ("Asia Pacific (Jakarta)", "ID"),
    "ap-southeast-4": ("Asia Pacific (Melbourne)", "AU"), "ap-southeast-5": ("Asia Pacific (Malaysia)", "MY"),
    "ap-southeast-7": ("Asia Pacific (Thailand)", "TH"),
    "ap-south-1": ("Asia Pacific (Mumbai)", "IN"), "ap-south-2": ("Asia Pacific (Hyderabad)", "IN"),
    "ap-east-1": ("Asia Pacific (Hong Kong)", "HK"),
    "me-south-1": ("Middle East (Bahrain)", "BH"), "me-central-1": ("Middle East (UAE)", "AE"),
    "il-central-1": ("Israel (Tel Aviv)", "IL"), "af-south-1": ("Africa (Cape Town)", "ZA"),
}
# Regions whose on-demand price list we download (one request each).
AWS_OD_REGIONS = ["us-east-1", "us-east-2", "us-west-2", "ca-central-1", "sa-east-1",
                  "eu-central-1", "eu-west-1", "eu-west-2", "eu-north-1", "ap-northeast-1",
                  "ap-northeast-2", "ap-southeast-1", "ap-southeast-2", "ap-south-1"]

# instance -> (gpu, gpu count, vram per GPU)
AWS_INSTANCES = {
    "p6-b300.48xlarge": ("B300", 8, 288), "p6-b200.48xlarge": ("B200", 8, 180),
    "p5en.48xlarge": ("H200", 8, 141), "p5e.48xlarge": ("H200", 8, 141),
    "p5.48xlarge": ("H100 SXM", 8, 80), "p5.4xlarge": ("H100 SXM", 1, 80),
    "p4de.24xlarge": ("A100 80GB", 8, 80), "p4d.24xlarge": ("A100 40GB", 8, 40),
    "g6e.xlarge": ("L40S", 1, 48), "g6e.12xlarge": ("L40S", 4, 48), "g6e.48xlarge": ("L40S", 8, 48),
    "g6.xlarge": ("L4", 1, 24), "g6.12xlarge": ("L4", 4, 24), "g6.48xlarge": ("L4", 8, 24),
    "g5.xlarge": ("A10G", 1, 24), "g5.12xlarge": ("A10G", 4, 24), "g5.48xlarge": ("A10G", 8, 24),
    "g4dn.xlarge": ("T4", 1, 16), "g4dn.12xlarge": ("T4", 4, 16), "g4dn.metal": ("T4", 8, 16),
    "p3.2xlarge": ("V100", 1, 16), "p3.8xlarge": ("V100", 4, 16), "p3.16xlarge": ("V100", 8, 16),
}

AZURE_SKUS = {
    "Standard_ND96isr_H200_v5": ("H200", 8, 141),
    "Standard_ND96isr_H100_v5": ("H100 SXM", 8, 80),
    "Standard_NC40ads_H100_v5": ("H100 NVL", 1, 94),
    "Standard_NC80adis_H100_v5": ("H100 NVL", 2, 94),
    "Standard_ND96is_MI300X_v5": ("MI300X", 8, 192),
    "Standard_ND96amsr_A100_v4": ("A100 80GB", 8, 80),
    "Standard_ND96asr_v4": ("A100 40GB", 8, 40),
    "Standard_NC24ads_A100_v4": ("A100 80GB", 1, 80),
    "Standard_NC96ads_A100_v4": ("A100 80GB", 4, 80),
    "Standard_NV36ads_A10_v5": ("A10", 1, 24),
    "Standard_NC4as_T4_v3": ("T4", 1, 16),
    "Standard_NC64as_T4_v3": ("T4", 4, 16),
    "Standard_NC6s_v3": ("V100", 1, 16),
    "Standard_NC24s_v3": ("V100", 4, 16),
}
AZURE_COUNTRY = {
    "US": "US", "CA": "CA", "MX": "MX", "BR": "BR", "CL": "CL", "EU": None, "UK": "GB",
    "FR": "FR", "DE": "DE", "SE": "SE", "NO": "NO", "CH": "CH", "PL": "PL", "IT": "IT",
    "ES": "ES", "AT": "AT", "DK": "DK", "BE": "BE", "FI": "FI", "AP": None, "JA": "JP",
    "KR": "KR", "AU": "AU", "IN": "IN", "NZ": "NZ", "ID": "ID", "MY": "MY", "TW": "TW",
    "AE": "AE", "QA": "QA", "IL": "IL", "SA": "SA", "ZA": "ZA",
}
AZURE_GEO_PREFIX = {"EU": "Europe", "AP": "Asia-Pacific"}


def row(provider, provider_type, gpu_raw, gpu, gpus, vram, pricing, price_hr, region,
        country, instance, rid, host=None, reliability=None, geo=None):
    return {
        "id": rid,
        "provider": provider,
        "provider_type": provider_type,
        "gpu": gpu,
        "gpu_raw": gpu_raw,
        "segment": segment(gpu),
        "vendor": vendor(gpu),
        "vram_gb": round(vram) if vram else None,
        "gpus": gpus,
        "pricing": pricing,
        "host": host,
        "price_hr": round(price_hr, 4),
        "price_gpu_hr": round(price_hr / gpus, 4),
        "region": region,
        "country": country,
        "geo": geo or geo_of(country),
        "instance": instance,
        "reliability": reliability,
    }


# --------------------------------------------------------------------------
# Providers

VAST_NAMES = ["B300", "B200", "H200", "H200 NVL", "H100 SXM", "H100 PCIE", "H100 NVL",
              "A100 SXM4", "A100 PCIE", "A800 PCIE", "L40S", "L40", "L4", "A40", "A10",
              "Tesla T4", "Tesla V100", "RTX PRO 6000 WS", "RTX PRO 6000 S", "RTX PRO 6000 Max-Q",
              "RTX PRO 5000", "RTX 6000Ada", "RTX A6000", "RTX A5000", "RTX A4000",
              "Q RTX 8000", "RTX 5090", "RTX 5080", "RTX 5070 Ti", "RTX 4090", "RTX 4080",
              "RTX 4070", "RTX 3090", "RTX 3080", "RTX 3060"]
VAST_URL = "https://console.vast.ai/api/v0/bundles/"


def vast_query(name, gpus_filter):
    q = {"rentable": {"eq": True}, "rented": {"eq": False}, "gpu_name": {"eq": name},
         "num_gpus": gpus_filter, "limit": 64, "type": "on-demand"}
    return http_json(VAST_URL, q).get("offers", [])


def fetch_vast():
    jobs = [(n, {"eq": 1}) for n in VAST_NAMES] + [(n, {"gte": 2}) for n in VAST_NAMES]
    offers = {}
    with cf.ThreadPoolExecutor(6) as ex:
        for res in ex.map(lambda j: vast_query(*j), jobs):
            for o in res:
                offers[o["id"]] = o
    rows = []
    for o in offers.values():
        n = int(o.get("num_gpus") or 1)
        vram = (o.get("gpu_ram") or 0) / 1024
        gpu = norm_gpu(o["gpu_name"], vram)
        loc = o.get("geolocation") or ""
        country = loc.split(",")[-1].strip().upper() if "," in loc else None
        region = loc.split(",")[0].strip() if loc else "Unknown"
        host = "Datacenter" if o.get("hosting_type") == 1 else "Community"
        rel = round(o["reliability"], 4) if o.get("reliability") is not None else None
        inst = f"{n}x {o['gpu_name']} · offer {o['id']}"
        if o.get("dph_total"):
            rows.append(row("Vast.ai", "Marketplace", o["gpu_name"], gpu, n, vram, "On-demand",
                            o["dph_total"], region, country, inst, f"vast-{o['id']}-od",
                            host, rel))
        if o.get("min_bid"):
            rows.append(row("Vast.ai", "Marketplace", o["gpu_name"], gpu, n, vram, "Spot",
                            o["min_bid"], region, country, inst, f"vast-{o['id']}-spot",
                            host, rel))
    return rows


def fetch_runpod():
    q = ("query { gpuTypes { id displayName memoryInGb securePrice communityPrice "
         "secureSpotPrice communitySpotPrice lowestPrice(input:{gpuCount:1}) "
         "{ minimumBidPrice uninterruptablePrice } } }")
    data = http_json("https://api.runpod.io/graphql", {"query": q})["data"]["gpuTypes"]
    rows = []
    for g in data:
        if g["id"] in ("unknown",):
            continue
        gpu = norm_gpu(g["id"], g.get("memoryInGb"))
        vram = g.get("memoryInGb")
        slug = re.sub(r"[^a-z0-9]+", "-", g["id"].lower()).strip("-")
        prices = [
            ("On-demand", "Datacenter", g.get("securePrice"), "secure"),
            ("On-demand", "Community", g.get("communityPrice"), "community"),
            ("Spot", "Datacenter", g.get("secureSpotPrice"), "secure-spot"),
            ("Spot", "Community", g.get("communitySpotPrice"), "community-spot"),
        ]
        bid = (g.get("lowestPrice") or {}).get("minimumBidPrice")
        if bid and not g.get("secureSpotPrice") and not g.get("communitySpotPrice"):
            prices.append(("Spot", "Mixed", bid, "spot-bid"))
        for pricing, host, price, key in prices:
            if price and price > 0:
                rows.append(row("RunPod", "GPU cloud", g["id"], gpu, 1, vram, pricing, price,
                                "Global", None, f"1x {g['displayName']} ({key})",
                                f"runpod-{slug}-{key}", host, geo="Unspecified"))
    return rows


def fetch_datacrunch():
    data = http_json("https://api.datacrunch.io/v1/instance-types")
    rows = []
    for t in data:
        n = (t.get("gpu") or {}).get("number_of_gpus") or 0
        if n < 1:
            continue
        vram = ((t.get("gpu_memory") or {}).get("size_in_gigabytes") or 0) / n
        gpu = norm_gpu(t.get("name") or t.get("model") or "", vram)
        for pricing, key in (("On-demand", "price_per_hour"), ("Spot", "spot_price")):
            p = float(t.get(key) or 0)
            if p > 0:
                rows.append(row("DataCrunch", "GPU cloud", t.get("name"), gpu, n, vram, pricing,
                                p, "Finland / Iceland", None, t["instance_type"],
                                f"datacrunch-{t['instance_type']}-{'od' if key == 'price_per_hour' else 'spot'}",
                                "Datacenter", geo="Europe"))
    return rows


def fetch_azure():
    skus = " or ".join(f"armSkuName eq '{s}'" for s in AZURE_SKUS)
    flt = f"serviceName eq 'Virtual Machines' and priceType eq 'Consumption' and ({skus})"
    url = "https://prices.azure.com/api/retail/prices?" + urllib.parse.urlencode({"$filter": flt})
    rows, seen = [], set()
    while url:
        page = http_json(url)
        for it in page.get("Items", []):
            name = it.get("productName", "")
            sku = it.get("skuName", "")
            loc = it.get("location", "")
            if "Windows" in name or "Low Priority" in sku or "Gov" in loc or "DoD" in loc:
                continue
            if it.get("unitOfMeasure") != "1 Hour" or not it.get("retailPrice"):
                continue
            pricing = "Spot" if "Spot" in sku else "On-demand"
            key = (it["armSkuName"], it["armRegionName"], pricing)
            if key in seen:
                continue
            seen.add(key)
            gpu, n, vram = AZURE_SKUS[it["armSkuName"]]
            prefix = loc.split(" ")[0]
            country = AZURE_COUNTRY.get(prefix)
            geo = AZURE_GEO_PREFIX.get(prefix) or geo_of(country)
            rows.append(row("Azure", "Hyperscaler", it["armSkuName"], gpu, n, vram, pricing,
                            it["retailPrice"], it["armRegionName"], country, it["armSkuName"],
                            f"azure-{it['armRegionName']}-{it['armSkuName']}-{'spot' if pricing == 'Spot' else 'od'}",
                            "Datacenter", geo=geo))
        url = page.get("NextPageLink")
    return rows


def fetch_aws_od(region):
    # The price-list files name European regions "EU (...)", not "Europe (...)".
    loc = AWS_REGIONS[region][0].replace("Europe (", "EU (")
    url = ("https://b0.p.awsstatic.com/pricing/2.0/meteredUnitMaps/ec2/USD/current/"
           f"ec2-ondemand-without-sec-sel/{urllib.parse.quote(loc)}/Linux/index.json")
    data = json.loads(http(url))
    out = {}
    for items in data.get("regions", {}).values():
        for v in items.values():
            it = v.get("Instance Type")
            if it in AWS_INSTANCES and float(v.get("price") or 0) > 0:
                out[it] = float(v["price"])
    return region, out


def fetch_aws():
    rows = []

    def add(region, inst, price, pricing):
        gpu, n, vram = AWS_INSTANCES[inst]
        name, country = AWS_REGIONS.get(region, (region, None))
        rows.append(row("AWS", "Hyperscaler", inst, gpu, n, vram, pricing, price, region,
                        country, inst, f"aws-{region}-{inst}-{'spot' if pricing == 'Spot' else 'od'}",
                        "Datacenter"))

    with cf.ThreadPoolExecutor(6) as ex:
        futures = [ex.submit(fetch_aws_od, r) for r in AWS_OD_REGIONS]
        for fut in futures:
            try:
                region, prices = fut.result()
            except Exception as e:
                print(f"AWS on-demand region skipped: {e!r}", file=sys.stderr)
                continue
            for inst, p in prices.items():
                add(region, inst, p, "On-demand")
    t = http("https://website.spot.ec2.aws.a2z.com/spot.js")
    spot = json.loads(t[t.index("(") + 1:t.rindex(")")])
    for r in spot["config"]["regions"]:
        for fam in r.get("instanceTypes", []):
            for s in fam.get("sizes", []):
                if s["size"] not in AWS_INSTANCES:
                    continue
                for col in s.get("valueColumns", []):
                    if col["name"] == "linux":
                        try:
                            p = float(col["prices"]["USD"])
                        except (ValueError, KeyError):
                            continue
                        if p > 0:
                            add(r["region"], s["size"], p, "Spot")
    return rows


PROVIDERS = [("Vast.ai", fetch_vast), ("RunPod", fetch_runpod), ("DataCrunch", fetch_datacrunch),
             ("Azure", fetch_azure), ("AWS", fetch_aws)]


# --------------------------------------------------------------------------

def summarise(rows, run_at):
    """One history row per GPU and pricing tier, so an hourly refresh stays small."""
    groups = {}
    for r in rows:
        groups.setdefault((r["gpu"], r["pricing"]), []).append(r)
    out = []
    for (gpu, pricing), rs in sorted(groups.items()):
        ps = sorted(r["price_gpu_hr"] for r in rs)
        cheapest = min(rs, key=lambda r: r["price_gpu_hr"])
        out.append({"run_at": run_at, "gpu": gpu, "segment": segment(gpu), "pricing": pricing,
                    "offers": len(ps), "min_gpu_hr": ps[0],
                    "median_gpu_hr": round(statistics.median(ps), 4),
                    "min_provider": cheapest["provider"]})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--history", help="previous history.json to append to")
    ap.add_argument("--keep-days", type=int, default=14)
    args = ap.parse_args()

    run_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    rows, failed = [], []
    for name, fn in PROVIDERS:
        try:
            got = fn()
            for r in got:
                r["fetched_at"] = run_at
            rows += got
            print(f"{name}: {len(got)} rows", file=sys.stderr)
        except Exception as e:  # keep the other providers when one is down
            failed.append(name)
            print(f"{name}: FAILED {e!r}", file=sys.stderr)

    rows.sort(key=lambda r: (r["gpu"], r["pricing"], r["price_gpu_hr"]))
    os.makedirs(args.out_dir, exist_ok=True)
    with open(os.path.join(args.out_dir, "offers.json"), "w") as f:
        json.dump(rows, f, separators=(",", ":"))

    history = []
    if args.history and os.path.exists(args.history):
        with open(args.history) as f:
            prev = json.load(f)
        history = prev.get("rows", prev) if isinstance(prev, dict) else prev
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=args.keep_days)).isoformat()
    history = [h for h in history if h["run_at"] >= cutoff[:19]]
    history += summarise(rows, run_at)
    with open(os.path.join(args.out_dir, "history.json"), "w") as f:
        json.dump(history, f, separators=(",", ":"))

    print(json.dumps({"run_at": run_at, "offers": len(rows), "history_rows": len(history),
                      "failed": failed}))
    return 1 if len(failed) == len(PROVIDERS) else 0


if __name__ == "__main__":
    sys.exit(main())
