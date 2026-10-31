# Card authorization rates and acceptance-optimization features: Stripe, Adyen, Checkout.com, Braintree/PayPal (state as of late Oct 2026)

Labels used below:
- **[VENDOR]**: the PSP's own marketing or investor claim, with no independent audit.
- **[PARTNER/CUSTOMER]**: a claim made by a customer or partner on a PSP-hosted page.
- **[3RD-PARTY]**: analyst, press, or blog source.
- **[PRE-2024]**: the figure or data window predates 2024.
- **[UNVERIFIED]**: seen only in a search-engine summary. I could not confirm it on the primary page when I fetched it.

No PSP publishes its absolute portfolio-wide authorization rate (e.g., "our approval rate is 9x%"). Every published number is an *uplift*, and the baselines differ: "industry baselines", "prior processor", a control group, pre-feature performance, or token vs PAN.

---

## 1. Published or credibly reported auth-rate and uplift figures per PSP (baseline, sample, caveats)

### Takeaway
All four PSPs publish only vendor-reported uplift figures, and none publishes an absolute approval rate. The headline numbers cluster around **~1–4% average uplift**: Stripe Authorization Boost "3.8% average", Checkout.com Intelligent Acceptance "+3.8 pp average", Adyen Uplift "1.19% above industry baselines" and "+0.9 pp conversion" in H1 2026, and Braintree "4% average lift" / network tokens "+4.8 pp" [PRE-2024]. Higher "up to" numbers (6%, 9.5 pp, 10%) are cherry-picked maxima or single customers. The baselines are not comparable across PSPs, and only Checkout.com documents a control-group methodology publicly.

### Cited Findings

**Stripe**
- Authorization Boost page: "+3.8% on average" acceptance-rate uplift and "about 20% on average" of false declines recovered. The page gives no baseline, sample, timeframe or footnotes, and it also uses the same 3.8% as a "revenue" increase, so the metric is ambiguous. [VENDOR] — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- Sessions 2026 (April 29, 2026): new AI optimizations under Authorization Boost, including "Data Only authentication flows and PINless debit retries", "increase acceptance rates by an average of 3.8%" and lower processing costs by up to 3.3%. Stripe also previewed **A/B testing Authorization Boost against a merchant's existing payments performance**. [VENDOR] — [Stripe: Everything we announced at Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- The Sessions 2026 roadmap page phrases it as Auth Boost increasing auth rates "by close to 4% on average while simultaneously lowering your network costs by 3%". [VENDOR][UNVERIFIED wording, from search summary] — [Stripe Sessions 2026 product roadmap: Payments and Radar](https://stripe.com/sessions/2026/product-roadmap-payments-and)
- **Conflicting Stripe figure:** a localized Stripe authorization page (Mexico) cites a **2.2% average** uplift for the bundle (Adaptive Acceptance + network tokens + card account updater). This looks like an older figure that the 3.8% has superseded, but the page does not say. [VENDOR] — [Stripe authorization page (ja-mx)](https://stripe.com/ja-mx/payments/authorization); compare [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- **Enhanced Issuer Network** (Stripe shares Radar scores with participating issuers such as Capital One, Discover and Amex): "1%–2% authorization rate uplift on eligible volume" and up to 8% fraud reduction. "Eligible volume" is undefined. [VENDOR] — [Stripe Authorization Boost](https://stripe.com/authorization-boost); [Stripe newsroom: Enhanced Issuer Network](https://stripe.com/newsroom/news/enhanced-issuer-network)
- Adaptive Acceptance recovered "a record-high $6 billion in falsely declined transactions" in 2024, "reflecting a 60% year-over-year increase in the retry success rate". This is an absolute recovery figure, not a rate. [VENDOR] — [Stripe blog: AI enhancements to Adaptive Acceptance](https://stripe.com/pt-pt/blog/ai-enhancements-to-adaptive-acceptance)
- Customer quotes on Stripe pages:
  - Notion: +1.9% acceptance rate.
  - Twilio SendGrid: +2% *conversion*, which is not the authorization rate.
  - USMobile: network costs reduced >2%.
  [PARTNER/CUSTOMER] — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- Older Twilio case study: "Twilio increases its authorization rates by 10% with Stripe", with ~1% credited specifically to Adaptive Acceptance. The study is roughly 6 years old. [PARTNER/CUSTOMER][PRE-2024] — [Stripe newsroom: Twilio](https://stripe.com/newsroom/stories/twilio); [Twilio case study](https://stripe.com/customers/twilio)
- Third-party blog (June 2026): Zapier saw a combined ~4% auth uplift, mostly from card account updater, and network tokenization gives "~6%" for eligible merchants, attributed to a former Stripe employee. I could not trace either figure to a primary source. [3RD-PARTY][UNVERIFIED] — [Corgi Labs](https://www.corgilabs.ai/insights/tokenization-as-a-service)

**Adyen**
- Adyen Uplift launched in January 2025. On Feb 11, 2026 Adyen reported first-year results:
  - "6,500+ businesses" using Uplift.
  - "an average increase of 1.19% in payment conversion rates above standard industry baselines", up to 6% for some customers.
  - "lower payment costs by 9.4% on eligible traffic".
  - False positives (blocked legitimate transactions) reduced 42% on average.

  "Standard industry baselines" is undefined, and the release does not say whether 1.19% is relative or in percentage points. It gives no methodology or sample. [VENDOR] — [Adyen Personalize launch release, Feb 11, 2026 (via AAP/Cision)](https://aapnews.aap.com.au/news/cision20260211AE82745)
- H2 2025 results (Feb 12, 2026): "the Personalize pilots drove up to 6% conversion and up to 3% lower transaction costs". Note that the cost figure differs from the 9.4% above. [VENDOR] — [Adyen H2 2025 results release](https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2)
- H1 2026 results (Aug 13, 2026): Adyen "increased customer conversion by 0.9 percentage points on average by the end of H1" through Adyen Uplift and Dynamic Identification. This is the most recent investor-grade figure. Note that it measures *conversion*, not the authorization rate. [VENDOR] — [Adyen H1 2026 results release](https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne)
- The Uplift Optimize page shows a "Smart Payment Messaging" chart with an approval rate of +6.41% "between Bank B and Bank A". It gives no period, volume or methodology, so treat it as illustrative. [VENDOR] — [Adyen Uplift Optimize](https://www.adyen.com/uplift/optimize)
- An Adyen executive cited an average ~6% authorization lift on a podcast. This is a podcast summary, not a published study. [VENDOR][UNVERIFIED] — [Tearsheet podcast](https://tearsheet.co/podcasts/taking-the-hardest-path-in-payments-how-adyens-new-ai-platform-boosts-conversion-while-reducing-fraud/)
- Tokenize page: customer Klook saw +3% authorization. [PARTNER/CUSTOMER] — [Adyen Uplift Tokenize](https://www.adyen.com/uplift/tokenize)
- Authenticate upgrade: 11% payment-conversion uplift in "early data". [VENDOR][UNVERIFIED, trade-press summary] — [UpTech Media](https://uptech-media.com/adyen-expands-uplift-suite-with-authentication-upgrade-built-on-trillions-of-transactions/)
- Network tokens (Sept 2023): Adyen reported 2B+ active network tokens and an average 3% authorization uplift across customers using them, plus an additional 1% from its token-optimization feature. [VENDOR][PRE-2024] — [Adyen press: two billion network tokens](https://www.adyen.com/press-and-media/adyen-has-issued-over-two-billion-active-network-tokens)
- Visa's case study on Adyen reports a 2–7% authorization uplift for tokens over PAN, by region:
  - US 4.74%
  - UK 2.80%
  - Brazil 3.23%
  - Australia 7.03%
  - Bahrain 3.70%

  [VENDOR (network)][PRE-2024, likely] — [Visa/Adyen case study PDF](https://usa.visa.com/dam/VCOM/global/products/documents/adyen-case-study.pdf)
- US debit Intelligent Payment Routing (announced Sept 9, 2024): a pilot with 20+ enterprise merchants (eBay, 24 Hour Fitness, Microsoft and others) achieved "an average of 26% cost savings with a 0.22% uplift in authorization rates". [VENDOR] — [Adyen press: Intelligent Payment Routing US debit](https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit); [Digital Transactions](https://www.digitaltransactions.net/adyen-rolls-out-intelligent-routing-in-response-to-debit-network-choice/)
- A review site claims enterprise customers "consistently" report a 0.5–2% improvement over their prior processors. It gives no source. [3RD-PARTY][UNVERIFIED] — [FinanceCopilotHQ Adyen review](https://financecopilothq.com/adyen-review-2026-payment-acquiring-financecopilothq/)

**Checkout.com**
- Blog of July 13, 2026: Intelligent Acceptance gives an average acceptance uplift of **+3.8 percentage points** "across the merchant portfolio".
  - Other figures in the post: 200+ live experiments at any time, each against a control group; ~70% of payments run on optimizations that began as experiments; **10.5 billion** optimizations in 2025; **$11.2B** merchant revenue recovered in 2025; **$2.2B** in the "first few months of 2026".
  - The post does not state the baseline or measurement window. [VENDOR] — [Checkout.com blog: How we built an AI payment optimization system](https://www.checkout.com/blog/smart-ai-payment-optimization)
- Launch (June 2023): in beta, acceptance rose by "up to 9.5 percentage points" for 30+ merchants, generating ~$750M in new revenue. [VENDOR][PRE-2024] — [PR Newswire launch release](https://www.prnewswire.com/news-releases/checkoutcom-launches-intelligent-acceptance-an-ai-powered-optimization-engine-that-boosts-acceptance-rates-and-increases-merchant-revenue-301863558.html); [FinTech Global](https://fintech.global/2023/06/27/checkout-com-unveils-ai-powered-optimisation-engine-to-boost-merchant-revenue/)
- March 2025: >$10B in cumulative additional merchant revenue since launch, and Sacra cites ~60M real-time optimizations per day. [VENDOR via 3RD-PARTY] — [Sacra Checkout.com profile](https://sacra.com/c/checkout-com/)
- **Methodology (unique among the four):** Checkout.com docs define "Total boost = First attempt boost + Reattempts boost".
  - The first-attempt boost is *estimated* against "a small unoptimized control group", with a statistical significance check.
  - The reattempt boost is *exact*: transactions declined on the first attempt and approved on retry.

  [VENDOR] — [Checkout.com docs: Boost acceptance rates](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- Klarna case study: +0.15% acceptance from issuer-specific network-token-vs-PAN selection, with automatic real-time PAN retry when a token is declined. [PARTNER/CUSTOMER] — [Checkout.com Klarna case study](https://www.checkout.com/case-studies/klarna-is-ensuring-seamless-experiences-for-their-customers-while-accepting-more-transactions)
- Reach (partner) reports its authorization rate on Checkout.com rails rose "by nearly 10%" after go-live. [PARTNER/CUSTOMER] — [Checkout.com Reach case study (de)](https://www.checkout.com/de-de/case-studies/reach-ermoglicht-es-unternehmen-lokal-zu-bleiben-und-global-zu-verkaufen)
- A review notes that 3.8% is an average among relevant users, and that merchants with sophisticated internal logic may see less. It recommends judging on incremental profit, not uplift alone. [3RD-PARTY] — [WalletInvestor review](https://walletinvestor.com/news/finance-news/checkout-com-review-enterprise-payment-infrastructure-evaluated/)

**Braintree / PayPal (incl. unbranded processing)**
- Network tokens: PayPal "has shown it can help increase authorization rates by 4.8 percentage points for merchants". Footnote: "Comparative analysis of major global payments network and PayPal internal data from transactions over a 12-month period from Q4 2020-Q3 2021 in 8 markets (US, UK, DE, AU, FR, IT, ES, CA) across 12 verticals. (2022)". The footnote states no baseline values. [VENDOR][PRE-2024] — [PayPal: Network tokenization's impact on authorization](https://www.paypal.com/us/brc/article/network-tokenization-and-lifecycle-management)
- Braintree had tokenized 1B+ cards globally as of Aug 2023. [VENDOR][PRE-2024] — [PayPal newsroom](https://newsroom.paypal-corp.com/2023-08-15-PayPal-Braintree-Reaches-One-Billion-Cards-Tokenized-Globally)
- The Payment Optimization page shows a "4% average lift" in authorization rates in a hero graphic, with no baseline.
  - The WeSki case footnote reads: "Data is from PayPal Braintree, October 2022 – March 2023, and compared against WeSki's prior approval rate… These results may not be typical and may vary substantially by business."

  [VENDOR][PRE-2024 data window] — [PayPal Enterprise Payment Optimization (CA)](https://www.paypal.com/ca/enterprise/payment-processing/payment-optimization)
- A claim that Braintree raised authorization rates "by 3.8 percentage points in the US" (and ~4 pp globally) appeared in a search summary. The cited PayPal page contained **no** such figure when I fetched it. [UNVERIFIED] — [PayPal: enterprise growth payments platform](https://www.paypal.com/us/brc/article/enterprise-growth-payments-platform-the-stack)
- Fastlane (accelerated guest checkout) figures:
  - ~80% guest-checkout conversion for recognized Fastlane shoppers and ~32% faster checkout, "based on PayPal internal data from Apr 3–Jun 15, 2024".
  - Other PayPal pages cite ~67%.
  - One merchant case went from ~74% to ~86% conversion.

  These are **checkout conversion** figures, not card authorization. [VENDOR] — [PayPal: one-click guest checkout and conversions](https://www.paypal.com/us/brc/article/one-click-guest-checkout-and-conversions); [PayPal Fastlane ebook](https://www.paypalobjects.com/marketing/fastlane%20ebook%20round%202/PayPal%20Fastlane%20Ebook_Final.pdf)
- Unbranded Braintree in 2023: PayPal's pricing push targeted unbranded Braintree. Coverage said Braintree "offers better authorization rates than in the past", with no number given. [3RD-PARTY][PRE-2024] — [Payments Dive](https://www.paymentsdive.com/news/paypal-payments-pricing-power-smb-braintree/712122/)

**Side-by-side headline claims (all vendor-reported)**

| PSP | Headline uplift claim | Metric / baseline | Date of claim |
|---|---|---|---|
| Stripe | +3.8% avg acceptance (Authorization Boost); 1–2% via Enhanced Issuer Network; $6B false declines recovered (2024) | Undefined baseline; Mexico page says 2.2% | Apr 2026 (Sessions) |
| Adyen | +1.19% conversion vs "industry baselines" (2025); +0.9 pp conversion (H1 2026); 42% fewer false positives; +0.22% auth on US debit routing | Conversion, not auth; undefined baseline | Feb 2026, Aug 2026 |
| Checkout.com | +3.8 pp avg acceptance; $11.2B recovered (2025) | Control-group method documented | Jul 2026 |
| Braintree/PayPal | +4.8 pp from network tokens; "4% average lift" | 2020–21 and 2022–23 data windows | Pre-2024 data |

### Inferences
- The two "3.8" numbers (Stripe's "3.8%" and Checkout.com's "3.8 pp") are coincidental and not comparable. Stripe's could be relative or absolute and has no baseline. Checkout.com's is stated in percentage points against a control group.
- Adyen has moved its public KPI from *authorization rate* to *conversion*, which also captures payment-method ordering (Personalize) and Dynamic Identification. That makes its numbers the hardest to compare with card-auth uplift claims from the others.
- PayPal/Braintree's auth-uplift evidence is the most dated. Its recent marketing emphasizes Fastlane checkout conversion rather than card-auth metrics, and no PayPal Complete Payments–specific auth figure was found.
- Stripe's preview of A/B testing Authorization Boost against a merchant's existing setup is, along with Checkout.com's control-group dashboard, the closest thing to merchant-verifiable uplift measurement.

### Gaps
- No PSP publishes an absolute portfolio-wide authorization rate, overall or by region (US vs EU vs LatAm vs APAC).
- No PayPal Complete Payments (PPCP) or "PayPal Open" auth-rate figure was found. I also found no 2025–2026 PayPal earnings disclosure quantifying Braintree auth-rate gains.
- Stripe's 2025 annual letter (covering $1.9T total volume) appears to contain no auth-rate metrics. I found none in excerpts and did not fetch the full letter.
- Adyen's H1 2026 shareholder letter itself was not fetched; only the press release was. Network-token and authentication metrics for 2025–2026 were not found.
- It is unclear whether Stripe's 3.8% is relative or in percentage points, and why localized pages still show 2.2%.

---

## 2. Acceptance-optimization features by PSP and how they work

### Takeaway
All four now offer the core stack: network tokens, account updater, ML retries, ML message tuning, 3DS/exemption optimization, and analytics. They differ in four places:
- **Acquiring and routing footprint.** Adyen and Checkout.com run their own multi-country acquiring and route across it. Stripe emphasizes direct network integrations and issuer data-sharing. Braintree has "Smart Routing"/"Direct Connect" across processors.
- **Explicit ISO 8583/issuer-preference tuning disclosure.** Checkout.com is the most explicit.
- **US debit (Durbin) routing.** Adyen has a quantified pilot, and Stripe added PINless debit retries in 2026.
- **Measurement transparency.** Checkout.com is the most transparent.

### Cited Findings

**Stripe (Authorization Boost bundle and adjacent features)**
- **Adaptive Acceptance:** ML adjusts "messaging, formatting, and retries to each issuer's preferences". Real-time false-decline recovery retries likely false declines "before the customer sees a decline", using signals from across the Stripe network. — [Stripe Authorization Boost](https://stripe.com/authorization-boost); [Stripe blog: AI enhancements to Adaptive Acceptance](https://stripe.com/pt-pt/blog/ai-enhancements-to-adaptive-acceptance)
- **Network tokens:** Visa, Mastercard and Amex. Stripe's AI decides when to retry with a token instead of the PAN. Stripe can provision tokens, or merchants can bring external ones. Tokens are on by default for Stripe Payments users. — [Stripe Authorization Boost](https://stripe.com/authorization-boost); [Stripe newsroom: network tokens & card account updater](https://stripe.com/newsroom/news/network-tokens-card-account-updater)
- **Card account updater:** real-time updates for replaced cards on Visa, Mastercard, Amex and Discover, including cross-brand updates. — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- **Decline prevention and excessive-retry prevention:** Stripe proactively declines charges likely to fail and stops retries that could trigger network penalties. — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- **Enhanced Issuer Network (issuer-facing data enrichment):** participating issuers (Capital One, Discover, Amex) get Radar fraud scores to inform their authorization decisions. — [Stripe Authorization Boost](https://stripe.com/authorization-boost); [Stripe newsroom](https://stripe.com/newsroom/news/enhanced-issuer-network)
- **2026 additions:**
  - "Data Only" authentication flows, which send 3DS data to the issuer without a challenge.
  - PINless debit retries.
  - Standalone 3DS with SCA exemption support, usable for payments processed by *another* PSP.
  - A Dashboard assistant that diagnoses acceptance issues.
  - A Link impact tab.
  - Roadmap: route Apple Pay through Australia's local eftpos network (Q2 GA).

  — [Stripe Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- **Pricing:**
  - Authorization Boost bundle: 0.2% per successful online card transaction, for accounts with custom pricing.
  - Adaptive Acceptance standalone: 0.08%.
  - Card account updater: $0.25 per update.
  - Network tokens: $0.15 per token provisioned, on IC+ pricing.
  - Up to 3.3% potential processing-cost reduction on IC+.

  — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- **Acceptance analytics:** Stripe has an Acceptance analytics dashboard in its docs. — [Stripe docs: Acceptance analytics](https://docs.stripe.com/payments/analytics/acceptance)
- **US debit:** Stripe's PINless explainer notes that the BIN determines the eligible networks and that PINless logic picks a regional network. High-risk categories and BINs without PINless enabled typically don't qualify. — [Stripe: PINless debit](https://stripe.com/resources/more/pinless-debit)

**Adyen (Uplift modules: Optimize, Protect, Authenticate, Tokenize, Personalize)**
- **Smart Payment Messaging:** tunes issuer messaging, e.g., CVC and AVS fields for low-risk transactions. On by default. — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement); [Adyen Uplift Optimize](https://www.adyen.com/uplift/optimize)
- **Intelligent Payment Routing:** ML picks the route by conversion or cost. It is off by default and needs ≥2 routes. In the US and Australia, merchants choose "balance" (recommended), "prioritize cost" or "prioritize conversion". This is the Durbin least-cost-routing lever; network-token and wallet transactions are eligible. — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement); [Adyen press: US debit routing](https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit)
- **Auto Retries and Auto Rescue:** Auto Retries adapt route, messaging, authentication and tokenization. Auto Rescue schedules retries of failed recurring payments to cut involuntary churn. — [Adyen Uplift Optimize](https://www.adyen.com/uplift/optimize); [Adyen docs](https://docs.adyen.com/partners/uplift-enablement)
- **Excessive Retry Prevention Service (ERPS):** blocks retries that would incur Visa/Mastercard penalties. It is opt-in and in maintenance mode, and Adyen states it "may have a negative impact on authorization rates". — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)
- **Tokenize:**
  - Network tokens, configured with the partner manager.
  - Real Time Account Updater: paid, sends no webhooks, and updated details arrive in the payment response.
  - Batch Account Updater: "not recommended".

  — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)
- **Authenticate:**
  - Native and redirect 3DS2.
  - Per-transaction 3DS overrides and rule-based dynamic 3DS.
  - An Authentication Engine that decides when to apply 3DS, with risk-based authentication on by default with Protect premium.

  — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)
- **Enhanced Scheme Data (L2/L3):** lowers interchange on qualifying US domestic card payments. Co-badged card support is also listed. — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)
- **Personalize:** dynamic payment-method ordering, A/B experiments, and a shopper conversion ID. — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)
- **Footprint:** Adyen holds full banking licences in the US, UK and EU. — [Adyen Uplift Optimize](https://www.adyen.com/uplift/optimize)

**Checkout.com (Intelligent Acceptance)**
- **Engine:** "self-learning" and based on **multi-armed bandit** algorithms that balance acceptance, cost and fraud. It covers five categories, listed in the bullets below. Enablement is via the account manager; no public pricing is given. — [Checkout.com docs: Boost acceptance rates](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- **Authentication management:**
  - Chooses between authentication and authorization channels based on historical issuer performance.
  - Selects the best-performing exemption (TRA, low-value).
  - Requests challenge or frictionless per issuer preference.
  - Picks the 3DS protocol version with the highest success odds.

  — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- **Regional example:** some French banks vary their exemption preference by transaction size, and a strategy that helps Visa in the US can hurt Mastercard in Germany. — [Checkout.com blog, Jul 2026](https://www.checkout.com/blog/smart-ai-payment-optimization)
- **Network token vs PAN:** a token is used only if the issuer supports it *and* approval odds are higher *and* predicted cost is lower. Sync vs async provisioning is also chosen, and the engine falls back to PAN if the issuer mishandles the token. — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- **Adaptive messaging:** adjusts request fields to scheme and issuer preferences, e.g., formatting billing addresses so AVS passes. The blog says it adapts to issuers' ISO 8583 preferences on "field values, standards, and field length". — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md); [Checkout.com blog](https://www.checkout.com/blog/smart-ai-payment-optimization)
- **Dynamic routing:**
  - Routes across "debit, local, or global networks" by predicted acceptance and the merchant's goals.
  - Updates credentials on the first attempt.
  - Applies "smart downgrades" for Account Funding Transactions.

  — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- **Intelligent retries:**
  - Fixes technical declines and retries.
  - Retries on an alternative network.
  - Handles SCA soft declines with new authentication routes or a step-up to a 3DS challenge.
  - Updates credentials via Real-Time Account Updater.
  - Falls back from token to PAN.

  — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)
- **Analytics:**
  - Dashboard under Payments > Analytics > Intelligent acceptance, showing revenue boost, transactions saved, AR boost by attempt and by optimization, and retry performance by original decline code.
  - A per-transaction "Payment optimized" webhook.
  - Governance: AI agents propose changes and a payments expert approves them.

  — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md); [Checkout.com blog](https://www.checkout.com/blog/smart-ai-payment-optimization)
- **Acquiring footprint:**
  - US direct acquiring went live Sept 9, 2026 under a Georgia Merchant Acquirer Limited Purpose Bank (MALPB) charter. The release makes no auth-rate claim. — [Checkout.com newsroom](https://www.checkout.com/newsroom/checkout-com-goes-live-with-us-direct-acquiring-under-malpb-charter)
  - UAE acquiring licence (2023), and domestic scheme Jaywan acceptance added in Sept 2026. — [Checkout.com UAE licence](https://www.checkout.com/en-ae/news/checkout-com-becomes-the-first-global-payments-platform-to-secure-acquiring-license-from-the-uae-central-bank); [The Paypers: Jaywan](https://thepaypers.com/payments/news/checkoutcom-adds-jaywan-domestic-card-scheme-acceptance-in-the-uae)
  - Canada direct acquiring. — [Yahoo Finance](https://finance.yahoo.com/news/checkout-com-introduces-direct-acquiring-113537836.html)
  - Third-party sources put local acquiring at ~50–55 countries and conflict with each other. [3RD-PARTY] — [Shuttle](https://www.shuttleglobal.com/payment-providers/checkout-com/)

**Braintree / PayPal**
- Features listed on the Payment Optimization page:
  - **Network Tokenization**, with real-time dynamic updates.
  - **Account Updater**, batch and real-time.
  - **Smart Retries**, driven by customer behavior, transaction history and processing performance.
  - **3DS**, for liability shift and SCA.
  - **Smart Routing**, which uses ML to predict the best path for primary and retry transactions, for both auth and cost.
  - **Direct Connect**, which adds processor options for redundancy against timeouts and outages.

  — [PayPal Enterprise Payment Optimization](https://www.paypal.com/ca/enterprise/payment-processing/payment-optimization)
- **Network tokens:** available to merchants "in the United States and select regions in North America, South America, and Europe who are processing full stack with Braintree", with no integration change. Apple Pay and Google Pay tokens are not transferable between providers. — [Braintree docs: Network tokens overview](https://developer.paypal.com/braintree/docs/guides/network-tokens/overview/)
- **Lifecycle management:** Braintree auto-refreshes network tokens on expiry or address change. — [PayPal: Network tokenization](https://www.paypal.com/us/brc/article/network-tokenization-and-lifecycle-management)
- **Fastlane:** email-recognized one-click guest checkout. This is a conversion lever, not an authorization lever. — [PayPal Fastlane ebook](https://www.paypalobjects.com/marketing/fastlane%20ebook%20round%202/PayPal%20Fastlane%20Ebook_Final.pdf)

**US Durbin / PINless debit context (industry, not PSP-specific)**
- Per CMSPI, only 51.1% of US debit cards had PINless enabled; the year was not stated in the snippet. CMSPI says least-cost debit routing saves US merchants >$1B per year, and that a Fed letter cited ≥$2B per year if PINless were fully available. [3RD-PARTY consultancy] — [CMSPI: PINless routing post-Durbin](https://cmspi.com/pinless-routing-expectation-vs-reality-in-a-post-durbin-tokenized-world/); [CMSPI 101](https://cmspi.com/?p=1092)
- Routing to the cheapest network can carry weaker approval performance for some issuer mixes. [3RD-PARTY] — [PaymentsJournal: routing trade-offs](https://www.paymentsjournal.com/understanding-the-trade-offs-between-transaction-routing-options/amp/)

**Feature matrix** (✔ = publicly documented; "?" = not found in public sources)

| Feature | Stripe | Adyen | Checkout.com | Braintree/PayPal |
|---|---|---|---|---|
| Network tokens (VTS/MDES) | ✔ (V/MC/Amex) | ✔ | ✔ (issuer-aware token vs PAN) | ✔ (US + select regions, full-stack only) |
| Account updater | ✔ real-time incl. cross-brand | ✔ RTAU (paid); batch discouraged | ✔ RTAU | ✔ batch + real-time |
| ML retries | ✔ Adaptive Acceptance | ✔ Auto Retries / Auto Rescue | ✔ Intelligent retries | ✔ Smart Retries |
| Message/ISO field tuning | ✔ "messaging, formatting" | ✔ Smart Payment Messaging (CVC/AVS) | ✔ ISO 8583 field values/length, AVS formatting | ? not explicitly documented |
| Routing / cascading | Direct network integrations; eftpos (AU) roadmap | ✔ Intelligent Payment Routing (≥2 routes) | ✔ debit/local/global network routing + alt-network retry | ✔ Smart Routing + Direct Connect (multi-processor) |
| US debit / Durbin LCR | PINless debit retries (2026) | ✔ (pilot: 26% cost savings, +0.22% auth) | "debit" network routing (US acquiring live Sep 2026) | ? |
| 3DS / SCA exemption mgmt | ✔ incl. standalone 3DS, Data Only | ✔ Authentication Engine, dynamic 3DS | ✔ exemption selection, protocol version, soft-decline step-up | ✔ 3DS (exemption logic not detailed) |
| Issuer data enrichment | ✔ Enhanced Issuer Network (Radar scores to issuers) | Data sharing for interchange (L2/L3) | Issuer-preference tuning | ? |
| Excessive-retry guard | ✔ | ✔ ERPS (may lower auth) | ? | ? |
| Acceptance analytics | ✔ Acceptance analytics + AI assistant | ✔ (Customer Area) | ✔ control-group boost dashboard + webhook | ? |

### Inferences
- Checkout.com publishes the most mechanism detail: bandit algorithms, the token-use decision rule, retry taxonomy, ISO 8583 tuning and control-group measurement. Stripe publishes the most pricing transparency. Adyen publishes the most configuration detail, including candid caveats such as ERPS lowering auth.
- Stripe is differentiated by the issuer-side data loop (Enhanced Issuer Network) and by selling 3DS standalone for multi-PSP merchants.
- Adyen and Checkout.com are differentiated by owned acquiring licences and local routing. Checkout.com's US MALPB charter (Sept 2026) closes a former gap with Adyen in the US.
- Braintree's public feature documentation is thinner and older. Its multi-processor "Direct Connect" suggests it positions partly as an orchestration layer rather than purely on owned acquiring.

### Gaps
- No PSP publishes exactly which ISO 8583 data elements it modifies.
- Stripe's local acquiring country list and Braintree's US debit routing capability were not found in this pass.
- Braintree's 3DS exemption-optimization logic (TRA, low-value, MIT flagging) is not documented in the sources reviewed.
- Regional auth-rate splits (LatAm, APAC) for any PSP were not found. The only regional figures are Visa's Adyen token case (US, UK, BR, AU, BH) [PRE-2024 likely], and PayPal's 8-market network-token study [PRE-2024].

---

## 3. Built-in fraud tooling performance claims and how the fraud-vs-acceptance trade-off is tuned

### Takeaway
Each PSP publishes headline fraud-tool claims, all vendor-reported. None publishes an overall false-positive rate:
- Stripe Radar: "32% average fraud reduction".
- Adyen Uplift/Protect: "42% fewer false positives".
- PayPal Fraud Protection Advanced: "significant reduction in good customer declines", from a 2019–20 sample.
- Checkout.com Fraud Detection: only a 2022 dollar figure.

Tuning is mostly merchant-controlled (risk-score thresholds, rules, review queues, backtesting). Stripe and Adyen increasingly automate threshold-setting.

### Cited Findings

**Stripe Radar**
- Radar claims a "32%" average reduction in fraud, with no baseline or sample given. It says it is trained on "70+ trillion data points" and that a "92% likelihood a charge is from a card Stripe has seen before". Anthropic reported an 83% reduction in legitimate transactions wrongly blocked [PARTNER/CUSTOMER]. Forrester rated Radar 5/5 for fraud mitigation (with a Forrester non-endorsement disclaimer). No overall false-positive or precision figure is published. [VENDOR] — [Stripe Radar](https://stripe.com/radar)
- Custom Radar models (Sessions 2026) are trained on a business's own signals plus Stripe network data. Early adopters reportedly detect "at least 15% more fraud with no increase in false positives". [VENDOR][UNVERIFIED wording, from search summary] — [Stripe Sessions 2026 product roadmap](https://stripe.com/sessions/2026/product-roadmap-payments-and)
- Other 2026 additions and roadmap:
  - Targeted checkout interventions such as CAPTCHAs, which "reduce fraud while improving conversion".
  - Free-trial-abuse and bot/agent detection.
  - Radar scores for off-Stripe payments via API (Q2 GA).
  - **Automatic block-threshold adjustment (Q3 GA)**.
  - Platform-specific 0–100 thresholds (Q4 preview).

  — [Stripe Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026)
- Radar docs define "estimated false positive rate" as the estimated percentage of non-fraudulent payments blocked, derived from experiments across the Stripe network. When unsure, the docs recommend review rules as a safer start than block rules. — [Stripe docs: Radar rules](https://docs.stripe.com/radar/rules)
- Enhanced Issuer Network claims up to 8% fraud reduction alongside a 1–2% auth uplift. This links fraud scoring directly to issuer approval decisions. [VENDOR] — [Stripe Authorization Boost](https://stripe.com/authorization-boost)
- Third-party coverage notes that Radar's current false-positive rate is not disclosed. A competitor (Riskified) published a comparison, which is a biased source. [3RD-PARTY] — [RFP.wiki Stripe Radar](https://www.rfp.wiki/payments-fraud/fraud-detection/stripe-radar); [Riskified vs Stripe Radar](https://www.riskified.com/learning/ecommerce-fraud-prevention/riskified-vs-stripe-radar/)

**Adyen Protect (formerly RevenueProtect, now within Uplift)**
- In Uplift's first year, false positives (blocked legitimate transactions) fell **42% on average**. [VENDOR] — [Adyen release, Feb 11, 2026](https://aapnews.aap.com.au/news/cision20260211AE82745)
- Mechanics:
  - Configurable or fixed risk profiles per merchant account or per payment.
  - A device/behavior risk-data SDK (`riskData.clientData`).
  - Case management for manual review (Protect premium).
  - Risk-based dynamic 3DS on by default with Protect premium.

  Adyen states effective risk management means "fewer false declines". — [Adyen docs: Uplift enablement](https://docs.adyen.com/partners/uplift-enablement)

**Checkout.com Fraud Detection / Fraud Detection Pro**
- The only quantified claim found is that Fraud Detection saved merchants "over $1.95bn in potential fraudulent losses in 2022". Fraud Detection Pro is available globally. [VENDOR][PRE-2024] — [Finextra](https://www.finextra.com/pressarticle/94519/checkoutcom-launches-online-fraud-detection-tool); [Checkout.com newsroom: Fraud Detection Pro](https://cfworker-www.checkout.com/newsroom/checkout-com-launches-fraud-detection-pro-to-combat-rise-in-online-fraud)
- Intelligent Acceptance's bandit engine explicitly balances "acceptance, cost, and fraud". Proposed optimizations must report "fraud implications" before an expert approves them. [VENDOR] — [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md); [Checkout.com blog](https://www.checkout.com/blog/smart-ai-payment-optimization)

**Braintree / PayPal Fraud Protection Advanced (FPA)**
- FPA's claim is that "merchants may see a significant reduction in good customer declines". Footnote: "Based on data analysis of 107 merchants' card transactions (9 of which had existing fraud solutions) in high chargeback category (merchants with greater than 1% chargeback rate), from Nov 2019 through Jan 2020… Results may not be typical". [VENDOR][PRE-2024] — [PayPal: 5 ways FPA gives a competitive edge](https://pep.paypal.com/brc/article/competitive-edge-against-fraud)
- Tuning: merchants build custom filters per their risk tolerance and **backtest filter changes against historical transactions** before deploying them. — [PayPal: 5 ways FPA](https://pep.paypal.com/brc/article/competitive-edge-against-fraud)
- The FPA product page claims "12.8B digital identifiers" and "98.5% of buyers recognized" (Braintree/PayPal internal data, June 2024–May 2025), and ML risk scores on every transaction. It gives no chargeback or auth-performance figure. [VENDOR] — [PayPal Fraud Protection Advanced](https://paypal.com/enterprise/fraud-protection-advanced)
- A claim that FPA users saw "chargeback rates decreased by 68%" and "authorization rates improved on average by 6%" appeared only in a search summary. It was not on the fetched FPA pages. [UNVERIFIED] — [PayPal FPA](https://paypal.com/enterprise/fraud-protection-advanced)
- A partner page claims up to a 60% average reduction in fraud losses "without impacting the overall approval rate". [PARTNER][UNVERIFIED] — [Arc XP Braintree partner page](https://partners.arcxp.com/partners/braintree)
- Braintree's separate **Chargeback Protection** (fee-waiver/guarantee) product is mutually exclusive with Fraud Protection tools; enabling one disables the other. — [Braintree docs: Chargeback protection tools](https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/chargeback-protection)

### Inferences
- The industry framing has shifted from "fraud blocked" to "false positives reduced" (Adyen 42%, Stripe's Anthropic 83%, PayPal's "good customer declines"). That shift tracks with the PSPs bundling fraud tools into acceptance products.
- Stripe's automatic block-threshold adjustment (Q3 2026 GA) and Checkout.com's bandit balancing of fraud against acceptance point toward PSP-automated trade-off tuning. Adyen's risk profiles and Braintree's backtested filters keep it more merchant-configured.
- PayPal's FPA evidence is the oldest (2019–2020 sample, high-chargeback merchants only), which limits how much it applies to typical merchants.

### Gaps
- No PSP publishes fraud-tool precision/recall, overall false-positive rates, or chargeback-rate outcomes with methodology.
- No 2024+ quantified Checkout.com Fraud Detection performance claim was found.
- The 68% chargeback / +6% auth FPA figure could not be traced to a fetched page.

---

## 4. Independent assessments and merchant case studies comparing these PSPs' auth rates

### Takeaway
I found **no independent, controlled, published comparison** of authorization rates across Stripe, Adyen, Checkout.com and Braintree. The most "independent" artifact is the Forrester Wave: Merchant Payment Providers, Q1 2026, which rates capabilities, not measured auth rates. Comparison blogs repeat vendor claims and recommend that merchants A/B test on their own traffic.

### Cited Findings
- **Forrester Wave: Merchant Payment Providers, Q1 2026** (published ~Mar 5, 2026; nine providers evaluated):
  - Adyen, Stripe and Checkout.com were all named Leaders.
  - Adyen claims the top score in 14 of 24 criteria.
  - Stripe claims the highest scores on more criteria than any other provider.
  - Checkout.com claims it was the only vendor with the top Merchant Experience score.
  - Forrester says "pace of innovation" mainly separates providers.
  - PayPal/Braintree's placement was not found.

  This is analyst capability scoring, not auth-rate measurement. — [Forrester report page](https://www.forrester.com/report/the-forrester-wave-tm-merchant-payment-providers-q1-2026/RES191722); [Forrester blog: Three surprising insights](https://www.forrester.com/blogs/three-surprising-insights-from-forresters-payment-providers-wave); [Adyen press](https://www.adyen.com/en_SG/press-and-media/adyen-recognized-as-leader-in-merchant-payment-providers-evaluation); [Stripe newsroom](https://stripe.com/newsroom/news/stripe-named-a-leader-by-forrester-2026); [Checkout.com newsroom](https://www.checkout.com/newsroom/checkout-com-named-a-leader-by-global-analyst-firm-as-it-bets-on-agentic-commerce-and-grows-us-business)
- A 2026 pricing teardown lists the vendor claims (Adyen Uplift +6%, Stripe Auth Boost +3.8%, Checkout.com +3.8% avg / up to +9.5 pp). It states that "independent measurement on your own traffic is the only way to verify". [3RD-PARTY] — [PaymentBrief: Stripe vs Adyen vs Checkout.com 2026](https://paymentbrief.com/articles/stripe-vs-adyen-vs-checkout-2026-pricing-teardown/)
- Comparison blogs say:
  - Adyen's direct network connections "can sometimes get slightly better authorization rates".
  - Large merchants A/B testing Stripe and Adyen find both "high performers", with differences by geography and issuer.

  These are opinion pieces, and the publisher (Convesio) has a commercial interest. [3RD-PARTY] — [Convesio: Adyen vs Stripe](https://convesio.com/knowledgebase/article/adyen-vs-stripe/); [Convesio: Stripe vs Adyen vs Braintree](https://convesio.com/knowledgebase/article/payment-processor-comparison-stripe-adyen-braintree-convesiopay/)
- A payments consultant (former acquirer adviser) writes commentary on the "authorization rate battle" between acquirers. It is opinion, not a dataset. A Checkout.com-sponsored Oxford Economics survey (Sept 2023, 1,500 enterprises) found 50% of merchants don't receive raw response codes when a payment fails. That survey is vendor-sponsored and does not compare acquirers. [3RD-PARTY][PRE-2024 survey] — [Dwayne Gefferie: The Authorization Rate Battle](https://dwaynegefferie.substack.com/p/the-authorization-rate-battle); [Dwayne Gefferie: The Acquirer Divergence](https://dwaynegefferie.substack.com/p/the-acquirer-divergence)
- Network-level token benchmarks sometimes used as neutral reference points: Visa's case study on Adyen (2–7% token uplift by region), and PayPal's 8-market comparison against "a major global payments network" (4.8 pp). Both are vendor or network-produced and pre-2024. — [Visa/Adyen case study](https://usa.visa.com/dam/VCOM/global/products/documents/adyen-case-study.pdf); [PayPal network tokenization](https://www.paypal.com/us/brc/article/network-tokenization-and-lifecycle-management)
- PSPs now offer tools for merchant-run comparisons:
  - Stripe previewed A/B testing Authorization Boost against existing performance (Apr 2026).
  - Stripe sells standalone 3DS for payments processed by other PSPs.
  - Checkout.com's dashboard uses an unoptimized control group.

  — [Stripe Sessions 2026](https://stripe.com/blog/everything-we-announced-at-sessions-2026); [Checkout.com docs](https://www.checkout.com/docs/payments/optimize-payments/boost-acceptance-rates.md)

### Inferences
- Cross-PSP auth comparisons are effectively private. Multi-acquirer merchants and orchestrators (e.g., those running Adyen plus Checkout.com or Stripe) hold the data but do not publish it. The defensible public statement is "vendor-claimed average uplifts of ~1–4% on optimized volume, with results depending on geography, issuer mix and baseline sophistication".
- Merchants with already-optimized stacks should expect smaller incremental gains than the headline averages. Reviewers flag this explicitly for Checkout.com, and it follows logically for all four.

### Gaps
- No independent dataset, from academia, Edgar Dunn, Juniper, Gartner, or a published multi-acquirer merchant engineering blog, was found comparing realized auth rates across these four PSPs in 2024–2026.
- The full Forrester Wave scoring, including PayPal's placement and any acceptance-related criterion scores, sits behind a paywall and was not accessed.
- No regional (EU/UK SCA vs US vs LatAm vs APAC) head-to-head auth data was found for any pair of these PSPs.
