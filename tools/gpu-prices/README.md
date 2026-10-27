# GPU rental prices

`fetch_gpu_prices.py` pulls current GPU rental prices from public provider APIs
(no keys needed) and writes the two data files behind the **GPU Rental Prices**
dashboard:

| File | Rows |
|---|---|
| `offers.json` | One per priced offer: provider, GPU model, GPU class, VRAM, GPUs per instance, pricing tier (on-demand or spot), price per hour and per GPU-hour, region, host type |
| `history.json` | One per refresh, GPU model and pricing tier: offer count, lowest and median price per GPU-hour |

Providers: Vast.ai (marketplace), RunPod, DataCrunch, AWS (EC2 on-demand in 14
regions, spot everywhere) and Azure (retail VM prices).

```sh
python3 fetch_gpu_prices.py --out-dir out --history previous/history.json --keep-days 14
```

It uses only the Python standard library. A provider that fails is skipped and
named in the summary line; the script exits non-zero only when every provider fails.
