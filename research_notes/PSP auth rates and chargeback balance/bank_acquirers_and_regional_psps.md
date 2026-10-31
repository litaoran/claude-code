# Bank-owned/legacy acquirers and regional/emerging-market PSPs: authorization rates, acceptance-optimization features, and local vs. cross-border acquiring

Scope: Worldpay (Global Payments), Cybersource / Visa Acceptance Solutions, Fiserv (Carat/Clover/First Data), J.P. Morgan Payments, Nuvei, dLocal, EBANX, Razorpay, Juspay, Xendit, 2C2P. Research date: 31 Oct 2026.

Labeling convention used throughout:
- **[VENDOR]** = vendor marketing claim, no independent audit.
- **[NETWORK]** = Visa/Mastercard data (first-party but network-wide).
- **[3P-VENDOR]** = third-party blog/glossary written by another PSP or orchestrator (a competitor with a commercial interest); weak.
- **[PRE-2024]** = figure or data period older than 2024.
- **[SNIPPET]** = seen in a search-result summary only; the underlying page was not opened, so treat as unverified.

---

## Q1. What authorization rates or uplift claims does each provider publish (with baselines and caveats)?

### Takeaway
None of these providers publishes an audited, like-for-like authorization rate. What exists is a patchwork of vendor uplift claims, usually "up to X%," with no disclosed baseline. Typical headline uplifts are 4–10% for Fiserv Carat, 5.5% for Worldpay 3DS Flex in the US, about 10–16% for Nuvei local acquiring and routing, and 7–10 pp for EBANX network tokens in Colombia and Peru. Visa's network-token figures (+4.6% global CNP, +8% Europe) are the most-cited "anchor" numbers. I found no published auth-rate uplift figure from J.P. Morgan Payments, dLocal, Juspay or 2C2P.

### Cited Findings

**Ownership context (verified)**
- Global Payments legally closed its acquisition of Worldpay on **9 Jan 2026** and announced it on 12 Jan 2026. It bought the Worldpay interests held by GTCR and other equityholders for 43,268,041 newly issued GPN shares. In the same set of transactions it sold its Issuer Solutions business to FIS in exchange for FIS's Worldpay stake plus about $7.7bn. The Worldpay price was based on a **$24.25bn enterprise value**. The combined company serves more than 6M merchant locations and processes $3.7T in payment volume. — [Global Payments 8-K](https://www.sec.gov/Archives/edgar/data/1123360/000110465926002705/tm262856d1_8k.htm); [Global Payments press release, Business Wire, 12 Jan 2026](https://www.businesswire.com/news/home/20260112224066/en); [Open Banking Expo](https://www.openbankingexpo.com/news/global-payments-completes-acquisition-of-worldpay/)
- Implication: Worldpay is now a Global Payments unit and FIS no longer holds any Worldpay stake. Worldpay's "internal data, 2025" claims below were generated before Global Payments owned it.

**Worldpay (Global Payments)**
- **3DS Flex** picks 3DS or data-only authentication per transaction. Worldpay says "Earlier results show a **5.5% increase in authorization rates in the US**," sourced to "Worldpay internal data, 2025." [VENDOR] — [Worldpay Innovation Focus: Keep auth rates climbing](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
- **Enhanced issuer data sharing**: "Merchants can see **32% reduction in false declines** on average," sourced to "Worldpay internal data, based on Q3 2025." [VENDOR] — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
- **Capital One Direct Data Share (Oct 2024)**: the integration "could reduce false positive declines by **40%** on average." This is projected from Capital One's own internal results since it launched the program, so it is one issuer's data and a forward-looking estimate. [VENDOR/ISSUER] — [Worldpay press release](https://www.worldpay.com/en/press-releases/reducing-fraud-and-amping-authorizations-worldpay-and-capital); [Payment Expert](https://paymentexpert.com/2024/10/29/worldpay-capital-one-share-data-fraud/)
- Worldpay's authorization-rates insights article gives **no** regional or product auth-rate numbers. It says only that "even a modest 1% to 2% gain in approvals can deliver significant impact," with no baseline. [VENDOR] — [Worldpay: Authorization rates insights](https://worldpay.com/insights/articles/authorization-rates-insights)

**Cybersource / Visa Acceptance Solutions (Visa)**
- **Token Management Service (network tokens)**: "+8%" authorisation rate uplift "across Europe when compared to eCommerce PAN transactions." The footnote cites "Visa Analytics Platform 2023" and defines auth rate as approved authorisations divided by total attempts, counting only the first attempt of a unique transaction. [NETWORK] — [Visa Acceptance TMS (APAC page)](https://www.visaacceptance.com/en-ap/solutions/payment-services/token-management-service.html)
- On the same page, network tokens "can reduce fraud by an average of **28%**." The data is VisaNet, global, comparing FY19 Q4 with FY20 Q4 for merchants averaging about 1k CNP token transactions per month. [NETWORK][PRE-2024] — [Visa Acceptance TMS](https://www.visaacceptance.com/en-ap/solutions/payment-services/token-management-service.html)
- Visa's widely cited global figure is a **+4.6% CNP auth-rate lift** for tokens versus raw PAN. Cybersource's network-tokenization collateral sources its token-versus-PAN comparisons to "VisaNet, Jan–Mar 2022." [NETWORK][PRE-2024] [SNIPPET] — [Cybersource "Simplify network tokenization" PDF](https://global2.cybersource.com/content/dam/documents/en/simplify-network-tokenization.pdf); [Visa "A deep dive on tokens"](https://corporate.visa.com/content/dam/VCOM/corporate/solutions/documents/a-deep-dive-on-tokens.pdf)
- I found no Cybersource-specific authorization-rate figure published in 2025–2026. Decision Manager case studies report a 60% cut in manual reviews (an airline) and a 50% cut in fraud ratio (Shopline), but no approval-rate or false-decline figure (see Q4).

**Fiserv (Carat / First Data / Clover)**
- **Authorization optimization** "utilizes adaptive, rules-based logic and partnerships with issuing banks to increase approval rates by **up to 10%**." [VENDOR] — [Fiserv Carat optimization checklist (PDF)](https://www.carat.fiserv.com/content/dam/carat/us/en/pdf/optimization-checklist.pdf) [SNIPPET]; also repeated on [Carat PL optimization page](https://carat.fiserv.com/pl-pl/solutions/optimization) [SNIPPET]
- Other Carat pages say "**4–10%** increase in authorization approval rates" and a "5–15% reduction in declines." A separate case-study item says "**7%** increase in approval rates for enterprise companies." The German page shows "07%," which looks like a typo for 7%. These figures are inconsistent with each other, and none gives a baseline. [VENDOR][SNIPPET] — [Carat DE optimization page](https://www.carat.fiserv.com/de-de/solutions/optimization/); [Carat payment LP](https://merchants.fiserv.com/en-us/lp/carat/payment/)
- Carat's "How to optimize your commerce model" says proper routing management "can increase approval rates by **up to 5%**," and that network tokens "can save **10 basis points** per transaction and lift authorization rates by an incremental **2%**." [VENDOR][SNIPPET] — [Carat: How to optimize your commerce model](https://www.carat.fiserv.com/en-us/resources/how-to-optimize-your-commerce-model/)
- A 2019 First Data post says it helped "one of the largest digital-gaming brands drive a 10% increase in their recurring card payment authorizations." [VENDOR][PRE-2024][SNIPPET] — [PaymentsJournal: Boosting revenue by optimizing authorization rates](https://www.paymentsjournal.com/boosting-revenue-for-merchants-by-optimizing-authorization-rates/)
- When I opened Carat's APAC optimization page directly, it had **no** figures. It lists only "Increase Approval Rates," "Reduce False Declines" and "Retry" as headings. — [Carat APAC optimization](https://www.carat.fiserv.com/en-apac/solutions/optimization/)

**J.P. Morgan Payments**
- I found **no** published auth-rate uplift or network-token uplift figure from J.P. Morgan Payments. Its merchant guide says its data scientists deploy "**six levers to increase authorization rates and three levers to reduce costs**," with examples such as wallet clean-up and transaction timing, but gives no measured lift. [VENDOR] — [J.P. Morgan "Simplifying payments for your business" (PDF)](https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/simplifying-payments-for-your-business.pdf) [SNIPPET]
- A Dec 2023 J.P. Morgan Payments master class cites "1,000,000+ combinations of approval rates and 500+ MCCs that impact approval rates." That describes how complex the problem is; it is not an uplift claim. [VENDOR][PRE-2024] — [J.P. Morgan: Optimize authorization rates](https://digital.jpmorgan.com/optimize-authorization-rates-to-help-maximize-revenue/index.html). The page returned HTTP 401 when fetched, so this is from the search snippet.

**Nuvei**
- Nuvei's 2026 acceptance guide says "Merchants using local acquiring can see **up to 16% higher acceptance rates** versus relying on a single acquirer," with no region, baseline or method given. It also says cascading retries recover "**one in four** retried transactions," which is a recovery rate, not an uplift. [VENDOR] — [Nuvei 2026 guide to global payment acceptance](https://nuvei.com/posts/the-2026-guide-to-global-payment-acceptance-local-acquiring-approval-rates-cross-border-optimization)
- Mexico article (6 May 2026): direct local acquiring "often yield[s] authorization rates **20% to 30% higher** than cross-border routing." Its comparison table puts local at "typically **80%+**" and cross-border at "often **50–60%**." In the Caliente case study, moving to local infrastructure produced a "**10% increase** in transaction acceptance rates." No methodology is given. [VENDOR] — [Nuvei: Mexico direct acquiring vs cross-border](https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models)
- Nuvei's Global Expansion page claims a "**12% boost** in approval rates" from local acquiring, and a Virgin Atlantic case study shows "~**10%** approval rate uplift." [VENDOR][SNIPPET] — [Nuvei Global Expansion](https://www.nuvei.com/offers/global-expansion-b)
- Nuvei's July 2025 North America release claims "up to **3.5 percentage points**" of authorization improvement from PINless debit and least-cost routing in the US and Canada. [VENDOR][SNIPPET] — surfaced via search; primary release not opened.
- A third-party profile says Nuvei claims about a 10% average uplift from intelligent routing plus local acquiring, and holds local acquiring licenses in **50+ countries**. This is a weak source. [SNIPPET] — [altss.com Nuvei profile](https://altss.com/profile/nuvei)

**dLocal**
- I found **no** quantified approval-rate figure from dLocal. Its May 2025 PayPal partnership release says only that "By enabling local processing, businesses can increase the number of transactions approved because domestic cards are more likely to be accepted by local acquirers." [VENDOR] — [dLocal–PayPal press release](https://www.dlocal.com/press-releases/dlocal-and-paypal-expand-access-to-local-payments-across-emerging-markets)
- A search snippet attributes this line to a Q1 2026 dLocal shareholder letter: "Even within the global credit card schemes, local processing is key to maximizing authorization and conversion rates in emerging markets." The snippet mentions internal tests comparing local processing with international-only acquiring but shows no figures. [VENDOR][SNIPPET, unverified]
- Business context: cross-border volume grew about 75% versus about 35% for local-to-local, and cross-border was more than 50% of dLocal volume for the second straight quarter (Q2 2025). [3P analysis] — [FXC Intelligence: dLocal Q2 2025](https://www.fxcintel.com/research/reports/ct-dlocal-q2-2025-earnings)

**EBANX**
- EBANX's "Local Acquiring" explainer says that with international acquirers "the approval rate usually ranges from **30% to 50%**," while local acquirers "can generate approval rates from **70% to 90%**." It gives no source, methodology or date. [VENDOR] — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring)
- Network tokens for cross-border transactions (press release, 11 Dec 2025):
  - **Colombia**: token approval rate +10 pp versus non-token; 87% merchant adoption (111 companies); more than 2M transactions a month.
  - **Peru**: more than +7 pp overall. SaaS +8 pp, online education about +7 pp, social media more than +6 pp, retail and streaming about +3 pp. Seven in ten card transactions are tokenized. The average approval rate is above 80% in some verticals.
  - **Dominican Republic**: 93% approval on token transactions in the early phase, with no baseline.
  - Fraud and security declines fell "up to 86%" in multi-country tests, with no baseline.
  - Launch markets were Brazil and Chile. [VENDOR] — [EBANX press release, Dec 2025](https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions)
- EBANX says that in both its local and cross-border models "all transactions are processed locally, ensuring optimized approval rates." A "+10 pp" uplift for SaaS merchants appears on marketing pages. [VENDOR][SNIPPET] — [EBANX Card Processing](https://www.ebanx.com/en/card-processing). A Mastercard Advisors benchmark report for Brazil exists but is gated, so I could not see its methodology: [EBANX Mastercard Advisors report](https://ebanx.com/en/mastercard-advisors-report).

**Razorpay (India)**
- Razorpay's success-rate optimization blog, dated 5 May 2026, gives these figures, mostly without sources [VENDOR]:
  - Success rates by method: UPI about **99.2%** (about 0.8% technical decline, "as of November 2024"), cards **85–90%**, net banking **90–95%**, international cards **70–80%**. Elsewhere it gives "cross-border" as **86%**, which is internally inconsistent with the 70–80% figure.
  - Uplift levers: network tokens up to **+4.4%** approval, cascading with acquirer fallbacks **+14.8%** acceptance, automated retries recovering **15–20%** of failures (+3–5 pp overall), total optimization potential **8–12 pp**.
  - Segments: Indian D2C averages **68–74%**; Tier-3 cities **55–62%**.
  - — [Razorpay: Payment success rate optimization India](https://razorpay.com/blog/payment-success-rate-optimization-india/)
- Razorpay also claims a 10–15% success-rate uplift on global card transactions. [VENDOR][SNIPPET] — [Razorpay International Card Payments](https://razorpay.com/blog/razorpay-international-card-payments/)
- An agency blog claims Razorpay's card authorization rate was "92% in 2024 vs 80% industry average," with no primary source. Disregard. [UNVERIFIED] — [irpr.agency](https://irpr.agency/blog/which-is-the-payment-gateway-with-best-success-rate-in-cards)

**Juspay (India orchestrator)**
- I found no quantified success-rate uplift. Juspay describes "Dynamic Gateway Ordering," which uses reinforcement learning and statistical distribution to route each transaction to the best gateway in real time while sending a small share of traffic to others for exploration. It notes that **95%+ of merchants use rule-based ordering**, not the dynamic mode. Its headline quantified claim is a "50% reduction in payment costs," not a success-rate figure. [VENDOR] — [Juspay: Orchestrator & merchant-controlled routing engine](https://juspay.io/blog/juspay-orchestrator-and-merchant-controlled-routing-engine); [Juspay payment orchestration](https://juspay.io/payment-orchestration)

**APAC: Xendit, 2C2P**
- Xendit says merchants "enjoy up to **30% increased acceptance rates**," with no methodology, and promotes Dynamic 3D Secure for higher acceptance. [VENDOR][SNIPPET] — [Xendit card docs](https://docs.xendit.co/credit-cards)
- 2C2P: I found no published acceptance or approval data. [Gap]

**Network-token anchor figures (for context across providers)**
- Mastercard: about **+2.1%**. Adyen: about **+3%**. Checkout.com: "2–3% for most merchants," while another Checkout.com source cites +10.3 pp on tokenized versus PAN in 2025. All are [3P-VENDOR][SNIPPET] and vary widely by methodology. — [Checkout.com network tokens blog](https://www.checkout.com/blog/network-tokens-why-your-2024-payment-strategy-needs-them); [Evervault webinar Q&A](https://evervault.com/blog/evaluating-network-tokens-webinar-q-and-a)

### Inferences
- Uplift claims cluster in two bands. **Single-digit uplift** (about 2–10%) comes from tokens, routing, retries and 3DS optimization at mature-market acquirers (Worldpay, Fiserv, Visa). **Double-digit uplift** (10–30%, or 20–60 pp ranges) comes from moving cross-border CNP traffic onto local acquiring in emerging markets (EBANX, Nuvei-Mexico, Xendit). This pattern fits the idea that the acquiring-geography fix is worth far more than tuning within an acquirer.
- "Up to X%" claims with no baseline are often relative uplift (for example, 70% to 77% is +10%) rather than percentage points. The EBANX token claims are explicitly in pp; most others are ambiguous.
- Fiserv's figures for the same product are inconsistent (4–10%, up to 10%, 7%), which suggests marketing copy rather than one measured result.
- J.P. Morgan, a very large US merchant acquirer, publishes no quantified uplift. Its positioning is advisory ("levers," data scientists) rather than product-metric-led.

### Gaps
- No audited or third-party measurement of any of these providers' auth rates was found.
- No J.P. Morgan Payments quantified auth-rate or token uplift was found.
- No dLocal approval-rate number was found. The Q1 2026 shareholder letter was seen only as a snippet.
- No 2C2P data was found. No Juspay success-rate number was found.
- Fiserv's "Authorization Optimizer" name could not be confirmed. Carat uses "Payment Optimization" and "authorization optimization" language instead.
- I could not confirm whether Worldpay's "Authorisation Optimisation" or AuthMax figures changed after the Global Payments close. An AuthMax infographic exists ([PDF](https://www.worldpay.com/-/media/fisglobal/WorldPay/Docs/Solutions/AuthMax-Infographic.pdf)) but I did not open it.

---

## Q2. What acceptance-optimization features does each provider offer?

### Takeaway
The legacy acquirers (Worldpay, Fiserv, Cybersource, J.P. Morgan) compete on a common toolkit: network tokens, account updater or credential lifecycle, smart retries, 3DS optimization, debit routing, and issuer data-sharing programs. Worldpay's issuer partnerships (Capital One, Auth Max Preferred) are the most distinctive. The emerging-market PSPs (dLocal, EBANX, Nuvei LatAm, Razorpay/Juspay, Xendit) compete mainly on **in-country acquiring**, installments, and local payment methods that sidestep card declines entirely.

### Cited Findings

**Worldpay (Global Payments)**
- **3DS Flex**: dynamic choice between 3DS and data-only authentication. — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
- **Auth Max Preferred**: issuers relax certain decline rules for low-risk Worldpay transactions; "available exclusively to Worldpay customers." — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
- **Enhanced Boost**: AI that maximizes network-token usage and decides when and where to use each credential based on issuer performance. — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
- **Issuer data sharing** (for example, Capital One Direct Data Share) and **US debit routing**. — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing); [Worldpay–Capital One release](https://www.worldpay.com/en/press-releases/reducing-fraud-and-amping-authorizations-worldpay-and-capital)
- Worldpay's insights article also describes network tokens, account updater, smart retry, debit routing and fraud management, without figures. — [Worldpay: Authorization rates insights](https://worldpay.com/insights/articles/authorization-rates-insights)
- **FraudSight**: fraud models "trained on billions of transactions across 174 countries," informed by "more than 52 billion annual transactions." — [Worldpay: Authorization rates insights](https://worldpay.com/insights/articles/authorization-rates-insights)

**Cybersource / Visa Acceptance**
- **Token Management Service**: network tokens across 189 live markets and 8.5K enabled issuers, with more than 95% issuer coverage by payment volume and 7B+ tokens provisioned (all as of 10 Jul 2023 [PRE-2024]). Credentials are "automatically refreshed across channels" to keep recurring payments flowing, which is lifecycle management functioning like an account updater. — [Visa Acceptance TMS](https://www.visaacceptance.com/en-ap/solutions/payment-services/token-management-service.html)
- **Decision Manager + Payer Authentication** (3DS) is offered as a bundle. — [Cybersource DM + Payer Authentication](https://www.cas.cybersource.com/en/solutions/fraud-and-risk-management/decision-manager-plus-payer-authentication.html)

**Fiserv Carat**
- Features named: adaptive rules-based authorization logic, partnerships with issuing banks, transaction routing management, network tokens, retry, and passive-churn reduction (card-on-file updating). — [Carat optimization checklist](https://www.carat.fiserv.com/content/dam/carat/us/en/pdf/optimization-checklist.pdf) [SNIPPET]; [Carat: Reduce passive customer churn](https://www.carat.fiserv.com/en-us/resources/reduce-passive-customer-churn/); [Carat APAC optimization](https://www.carat.fiserv.com/en-apac/solutions/optimization/)

**J.P. Morgan Payments**
- Advisory "six levers" to increase authorization (including wallet clean-up and transaction timing), plus Safetech fraud and card-testing tools as a "multi-layer defense." — [J.P. Morgan merchant guide (PDF)](https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/simplifying-payments-for-your-business.pdf) [SNIPPET]

**Nuvei**
- Features: local acquiring network, smart routing ("billions of transaction data points," routing by issuer preference, authentication logic and card-brand behavior), cascading retries, dynamic 3DS / 3DS step-up, and network tokens. — [Nuvei 2026 guide](https://nuvei.com/posts/the-2026-guide-to-global-payment-acceptance-local-acquiring-approval-rates-cross-border-optimization)
- In Mexico, local acquiring gives "Full Support" for installments (MSI, *meses sin intereses*), whereas cross-border has "Limited or No Support." Nuvei says MSI plans "drive approximately **40%** of all e-commerce volume" in Mexico. Local settlement is in MXN; cross-border settlement is "often USD or EUR." It names Prosa and E-Global as the domestic rails. [VENDOR] — [Nuvei Mexico article](https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models)

**dLocal**
- Local processing for global card schemes plus local payment methods. Through the May 2025 PayPal partnership, local processing is offered to PayPal merchants. — [dLocal–PayPal release](https://www.dlocal.com/press-releases/dlocal-and-paypal-expand-access-to-local-payments-across-emerging-markets)

**EBANX**
- Local processing in both its "local" and "cross-border" models. [SNIPPET] — [EBANX Card Processing](https://www.ebanx.com/en/card-processing)
- Network tokens for cross-border transactions in Brazil, Chile, Colombia, Peru and the Dominican Republic (Dec 2025). — [EBANX Dec 2025 release](https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions)
- Same-day settlement with local acquirers. Cross-border fees (international interchange and assessments) are avoided. — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring)
- Integration partnerships with Worldpay and Spreedly, so that global acquirers can route LatAm traffic through EBANX. — [EBANX–Worldpay integration](https://www.ebanx.com/en/ebanx-worldpay-integration/); [EBANX & Spreedly](https://www.ebanx.com/en/ebanx-and-spreedly)

**Razorpay / Juspay (India)**
- Razorpay promotes network tokens, cascading with acquirer fallback, method-specific timeouts, automated retries, and UPI as a high-success alternative to cards. — [Razorpay success rate blog](https://razorpay.com/blog/payment-success-rate-optimization-india/)
- Juspay offers multi-gateway orchestration with rule-based or RL-driven dynamic gateway ordering. — [Juspay routing blog](https://juspay.io/blog/juspay-orchestrator-and-merchant-controlled-routing-engine)

**Xendit**
- Dynamic 3D Secure and card-acceptance integrations. — [Xendit card docs](https://docs.xendit.co/credit-cards)
- Xendit advertises 38+ payment methods. — [Xendit all payment methods](https://xendit.co/en-id/products/all-payment-methods/)
- Philippines onboarding requires a local entity (SEC/DTI and BIR registration), which suggests local acquiring is tied to entity setup. [SNIPPET] — [rfp.wiki Xendit](https://www.rfp.wiki/payments-fraud/xendit)

### Inferences
- Issuer-side programs (Worldpay Auth Max Preferred and Capital One data share; Fiserv "partnerships with issuing banks") only work at scale. They are a structural advantage of large bank-owned or legacy acquirers that pure-play gateways cannot easily copy.
- Installments are a feature cross-border acquiring frequently cannot support in Mexico (MSI) and Brazil (parcelado). Local acquiring matters beyond the auth rate itself, because without it the merchant may not be able to offer the payment option at all.

### Gaps
- I did not confirm a full feature matrix for each provider. Account-updater availability at J.P. Morgan, Nuvei, dLocal and EBANX was not verified from primary pages.
- I found no primary source on the Pix, Boleto, OXXO or UPI share of checkout for these PSPs in 2026. Razorpay's UPI 99.2% success is the only local-payment-method performance figure found.
- I did not verify Fiserv Clover-specific CNP optimization features.

---

## Q3. What are typical card-not-present authorization rates by region, and cross-border vs. domestic?

### Takeaway
Credible, independent, recent regional CNP benchmarks are scarce. The best network-sourced figure is old: Visa data from 2016–17 shows about 20% of e-commerce transactions declined in certain LatAm countries, versus 3% card-present. Vendor and PSP figures broadly agree on a few points. Domestic CNP sits roughly in the 80–95% range in mature markets. Cross-border CNP into emerging markets can drop to about 50–60% in LatAm (some vendors say 30–50%). India card success is about 85–90%, versus about 99% for UPI. I found no credible Africa or MENA figures.

### Cited Findings
- **LatAm (network data)**: "three out of 100" card-present transactions are declined in "certain Latin American countries," versus "two out of 10" card-not-present (e-commerce) transactions. Source: "VPS authorization dashboard based on Visanet data, April 2016 – March 2017." [NETWORK][PRE-2024] — [Visa Performance Solutions: Improving the credit authorization customer experience](https://caribbean.review.visa.com/partner-with-us/visa-performance-solutions/improving-the-credit-authorization-customer-experience.html)
- **LatAm (vendor)**: declines "typically range from 15% to 25%" in the region. [3P-VENDOR][SNIPPET] — [Rapyd: LATAM decline rates](https://www.rapyd.net/blog/payment-processing-decline-rates-in-latam/)
- **LatAm cross-border vs. local (vendor)**: Mexico local about 80%+ versus cross-border 50–60% [VENDOR] — [Nuvei Mexico](https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models). EBANX says international acquirers achieve 30–50% and local acquirers 70–90% [VENDOR] — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring).
- **Cross-border (Antom)**: cross-border card authorization rates average "below 60%." Context is unclear; Antom's LatAm material also cites a 3.9% regional e-commerce fraud rate versus a 3% global average. [3P-VENDOR][SNIPPET] — [Antom: Failed payments playbook](https://www.antom.com/merchant-playbook/failed-payments)
- **Asia**: cross-border merchants entering Asia "typically see authorization rates 5–10 percentage points below their home-market baseline." [3P-VENDOR][SNIPPET] — [Antom: How AI improves payment authorization rate](https://knowledge.antom.com/how-ai-improves-payment-authorization-rate)
- **India (Razorpay, May 2026)**: cards 85–90%, net banking 90–95%, UPI about 99.2% (Nov 2024), international cards 70–80%, D2C average 68–74%. [VENDOR] — [Razorpay](https://razorpay.com/blog/payment-success-rate-optimization-india/)
- **Mature markets (Fiserv Carat)**: CNP approval rates "hover around 80+%" versus card-present "95%+." [VENDOR][SNIPPET] — [Carat: How to optimize your commerce model](https://www.carat.fiserv.com/en-us/resources/how-to-optimize-your-commerce-model/)
- **Generic domestic vs. cross-border (glossaries and blogs from other PSPs and orchestrators)** [3P-VENDOR][SNIPPET]:
  - Domestic 95–99% versus cross-border 70–90%. Cross-border e-commerce 70–85%. Local acquiring lifts cross-border from 72–80% to 85–90%. Switching to local acquiring improves authorization by 2–15 pp depending on market. — [Spark: Local Acquiring](https://www.spark.money/glossary/local-acquiring); [Spark: Authorization rate](https://www.spark.money/glossary/authorization-rate)
  - Cross-border card declines of 15–25% versus 1–5% domestic. Local acquiring in Europe lifts approvals "up to 21%." — [Tazapay](https://tazapay.com/blog/reduce-cross-border-card-declines-local-acquiring); [PayerMax](https://www.payermax.com/article/knowledge/yuftet9xz8tkt5asiek1j95s)
  - International cards run "5 to 15 percentage points below domestic baselines." — [Yuno](https://www.y.uno/en/blog/the-real-cost-of-cross-border-authorization-latency)
- **Older regional cut [PRE-2024]**: Spreedly published a 2019 regional breakdown of credit card acceptance rates. I did not open it. — [Spreedly 2019 regional breakdown](https://spreedly.com/blog/credit-card-acceptance-rates-2019-regional-breakdown)

### Inferences
- The figures converge on a consistent picture. The CNP penalty versus card-present is about 5–15 pp in mature markets. The cross-border penalty is about 5–15 pp in mature and Asian markets and widens to about 20–40 pp in LatAm, where issuers are most conservative on foreign-acquired CNP.
- Sources conflict enough that only ranges should be used (for example, cross-border is "<60%" per Antom but "70–85%" per Spark). Definitions also differ: first-attempt versus all attempts, auth versus success rate, and issuer approval versus end-to-end success. Visa's footnote explicitly uses first-attempt auth rate ([Visa Acceptance TMS](https://www.visaacceptance.com/en-ap/solutions/payment-services/token-management-service.html)), while Indian sources such as Razorpay report end-to-end "success rate."

### Gaps
- I found no credible, recent (2024–2026) independent North America or Europe CNP auth-rate benchmark in this scope. Adjacent researchers may hold Visa/Mastercard or Stripe/Adyen data.
- I found no Africa or MENA CNP or cross-border auth-rate data from any credible source.
- No RBI or NPCI card success-rate statistics were found. The UPI 99.2% figure is Razorpay's, citing Nov 2024.
- PCMI and EBANX "Beyond Borders" reports were not reached. PCMI is cited only indirectly in the EBANX Dec 2025 release: about 60% of Peru e-commerce is via cards, and 84% of Dominican Republic digital transactions are by card. — [EBANX Dec 2025 release](https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions)

---

## Q4. How do these providers' fraud/risk tools position the fraud-prevention vs. false-decline trade-off?

### Takeaway
All four legacy players frame false declines as costlier than fraud and sell their fraud tools as approval-rate tools. Worldpay is the most quantified, with a 32% false-decline reduction (Q3 2025 internal data), a 40% figure from the Capital One issuer data share, and a claim that false declines cost about 3x fraud. Cybersource's quantified claims cover manual review and fraud ratio, not false declines. J.P. Morgan (Safetech) and Fiserv publish no current quantified false-decline claims.

### Cited Findings
- **Worldpay / FraudSight**:
  - Enhanced issuer data sharing gives a "32% reduction in false declines on average" (Worldpay internal data, Q3 2025). [VENDOR] — [Worldpay Innovation Focus](https://worldpay.com/en/innovation-focus/keep-auth-rates-climbing)
  - The Capital One data share "could reduce false positive declines by 40% on average" (Oct 2024, based on issuer internal data). [VENDOR] — [Worldpay–Capital One release](https://www.worldpay.com/en/press-releases/reducing-fraud-and-amping-authorizations-worldpay-and-capital)
  - Coverage of that release says about 6% of e-commerce transactions are rejected on suspicion of fraud and "up to 10%" of those are false declines. [SNIPPET] — [Fintech Times](https://thefintechtimes.com/capital-one-collaborates-with-worldpay-to-improve-payment-security-for-merchants/)
  - Worldpay's platforms fraud page says losses to false declines are "3x the cost of fraud itself" (internal data). [VENDOR][SNIPPET] — [Worldpay Platforms fraud prevention](https://platforms.worldpay.com/embedded-payments/fraud-prevention/)
  - The WorthPoint case is about card-testing defense: "stopped 60,000 fraudulent authorizations within 10 days." [VENDOR][SNIPPET] — [Worldpay WorthPoint case study](https://www.worldpay.com/en/insights/case-study/worthpoint)
- **Cybersource Decision Manager**:
  - An airline cut its manual review rate by 60%, and Shopline cut merchants' fraud ratio by 50% while claiming improved conversion. Neither reports a false-decline figure. [VENDOR][SNIPPET] — [Cybersource DM + Payer Authentication](https://www.cas.cybersource.com/en/solutions/fraud-and-risk-management/decision-manager-plus-payer-authentication.html); [Visa Acceptance Shopline case](https://www.visaacceptance.com/en-ap/case-studies/shopline.html)
  - The DM page frames the problem with Javelin research: 51% of falsely declined consumers used another card to complete the purchase. [SNIPPET] — same DM page.
  - Visa Acceptance describes its AI-driven fraud management as helping merchants "accept more good transactions." — [Visa Acceptance AI-driven fraud management](https://partners.cas.visaacceptance.com/en-us/solutions/ai-driven-fraud-management.html)
- **J.P. Morgan Safetech**: positioned as a "multi-layer defense" with fraud and card-testing tools. I found no quantified false-decline or approval claim. [VENDOR][SNIPPET] — [J.P. Morgan merchant guide](https://www.jpmorgan.com/content/dam/jpm/merchant-services/documents/simplifying-payments-for-your-business.pdf)
- **Fiserv**: Carat lists "Reduce False Declines" as a benefit with no figure ([Carat APAC optimization](https://www.carat.fiserv.com/en-apac/solutions/optimization/)). Older coverage includes a 2019 American Banker piece on how the First Data purchase could help Fiserv tackle false declines ([American Banker](https://www.americanbanker.com/payments/news/how-fiservs-purchase-of-first-data-helps-it-tackle-false-declines)) and a 2020 issuer-side product cutting legitimate debit transactions wrongly flagged as fraud ([Help Net Security, 2020](https://www.helpnetsecurity.com/2020/05/25/fiserv-authorization-lift/)). [PRE-2024][SNIPPET]
- **EBANX**: network tokens cut fraud and security declines by "up to 86%" in multi-country tests. [VENDOR] — [EBANX Dec 2025](https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions)
- **Razorpay**: frames false declines as costing more than they save. It says ₹100 saved in fraud versus ₹400–600 lost to false declines, unsourced. [VENDOR] — [Razorpay](https://razorpay.com/blog/payment-success-rate-optimization-india/)
- **Industry framing**: ClearSale, a competing fraud vendor, estimates false declines cost US merchants about $118B a year. [3P-VENDOR][SNIPPET] — [ClearSale](https://www.clear.sale/blog/everything-you-need-to-know-about-false-declines.json)

### Inferences
- The industry has shifted from "fraud screening" to "approval optimization." The newest Worldpay levers (issuer data sharing, Auth Max Preferred) act on the **issuer's** decision rather than the merchant's own fraud rules. That is the main remaining lever once merchant-side screening is tuned, and it suits large acquirers with issuer relationships.
- Quantified false-decline claims rest almost entirely on single-issuer or internal data (Capital One; Worldpay Q3 2025), so they cannot be generalized across issuers or regions.

### Gaps
- I found no independent measurement of false-decline rates for any of these tools.
- I found no current (2025–2026) quantified claim for J.P. Morgan Safetech, Fiserv merchant fraud tools, or the post-merger Global Payments combined fraud stack.

---

## Q5. Why does cross-border vs. local acquiring matter so much for auth rates in emerging markets (LatAm, India, SE Asia, Africa)?

### Takeaway
Issuers in emerging markets treat foreign-acquired CNP transactions as high-risk. Some domestic cards are not even enabled for international use. Cross-border acquiring also blocks local features such as installments, and it adds fees and FX friction. Every PSP source therefore reports a large gap, from about 20–30% relative in Mexico up to a 30–50% versus 70–90% split for LatAm, according to EBANX. All of these magnitudes are vendor claims, and the only network-sourced LatAm data is from 2016–17.

### Cited Findings
- **Issuer risk perception**: when a transaction arrives through an international acquirer, the issuer doesn't recognize it as local and lacks merchant and customer context, so it is more likely to decline. Local acquirers apply "less strict" risk rules. [VENDOR] — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring)
- **Domestic-only cards**: some domestic cards are not enabled for international purchases, so international-only acceptance cannot reach those cardholders at all. — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring)
- **Domestic cards favored by local acquirers**: "domestic cards are more likely to be accepted by local acquirers." [VENDOR] — [dLocal–PayPal release](https://www.dlocal.com/press-releases/dlocal-and-paypal-expand-access-to-local-payments-across-emerging-markets)
- **Mexico magnitude**: local about 80%+ versus cross-border about 50–60%, a 20–30% gap. Caliente gained +10% after moving local. Installments (MSI, about 40% of e-commerce volume) have "Limited or No Support" cross-border. [VENDOR] — [Nuvei Mexico](https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models)
- **LatAm network baseline**: CNP declines of about 20% versus 3% card-present in certain LatAm countries (VisaNet, Apr 2016 – Mar 2017). [NETWORK][PRE-2024] — [Visa VPS](https://caribbean.review.visa.com/partner-with-us/visa-performance-solutions/improving-the-credit-authorization-customer-experience.html)
- **Fees and settlement**: local acquiring avoids international interchange, scheme assessment fees and FX markups. It settles in local currency, same day per EBANX, versus "several working days" or "several days of delay" for international settlement. — [EBANX: Local Acquiring](https://www.ebanx.com/en/insights/payments-explained/local-acquiring); [Nuvei Mexico](https://www.nuvei.com/posts/evaluating-payment-strategies-for-the-mexican-market-direct-acquiring-versus-cross-border-models)
- **Local presence is a licensing and entity question**: Xendit's Philippines onboarding requires a PH entity. [SNIPPET] — [rfp.wiki Xendit](https://www.rfp.wiki/payments-fraud/xendit). Nuvei (per a third-party profile) holds local acquiring licenses in 50+ countries. [SNIPPET] — [altss Nuvei](https://altss.com/profile/nuvei)
- **Network tokens on cross-border flows**: EBANX reports +7 to +10 pp approval with tokens on cross-border transactions in Peru and Colombia. Tokens partly offset the issuer's "unknown foreign merchant" risk signal. [VENDOR] — [EBANX Dec 2025](https://business.ebanx.com/en/press-room/press-releases/ebanx-drives-the-next-phase-of-credit-cards-in-latam-with-network-tokenization-for-cross-border-transactions)
- **India**: international cards succeed at about 70–80% versus 85–90% for cards overall, and UPI at about 99.2%. This shows the local-rail alternative to cards in a low-card-auth market. [VENDOR] — [Razorpay](https://razorpay.com/blog/payment-success-rate-optimization-india/)
- **SE Asia**: cross-border merchants entering Asia see auth rates 5–10 pp below their home baseline. [3P-VENDOR][SNIPPET] — [Antom](https://knowledge.antom.com/how-ai-improves-payment-authorization-rate). Xendit claims up to 30% higher acceptance. [VENDOR][SNIPPET] — [Xendit docs](https://docs.xendit.co/credit-cards)
- **Strategic demand signal**: dLocal's cross-border volume (global merchants selling into emerging markets) grew about 75% year on year and exceeded 50% of total volume in Q2 2025. That suggests strong demand for "cross-border merchant, local processing" models. [3P analysis] — [FXC Intelligence](https://www.fxcintel.com/research/reports/ct-dlocal-q2-2025-earnings)

### Inferences
- The local-acquiring advantage has several causes, not one: issuer risk models, domestic-only BINs, unavailable installments, fee and FX costs, and settlement timing. Auth rate is the most visible symptom, but installments and domestic-only cards can mean a whole segment of buyers cannot be reached.
- Global acquirers mostly answer this through partnerships, for example Worldpay with EBANX ([EBANX–Worldpay integration](https://www.ebanx.com/en/ebanx-worldpay-integration/)), rather than their own EM licenses. Regional specialists and Nuvei sell their local licenses as the differentiator.
- Local payment methods (Pix, UPI, OXXO, Boleto) are the ultimate fallback in markets with low card authorization. UPI's about 99% technical success rate versus cards' 85–90% in India is the clearest evidence found.

### Gaps
- I found no independent (network or regulator) 2024–2026 measurement of the local-versus-cross-border approval gap for Brazil, India, Indonesia, the Philippines, Nigeria, Kenya, South Africa, or MENA markets.
- I found no Africa-specific data at all, from EBANX (which has Africa operations), dLocal, or others.
- I found no Pix, Boleto or OXXO conversion and approval data from these PSPs. RBI and NPCI official success-rate data was not retrieved.
- The Brazil approval-rate benchmark (EBANX Mastercard Advisors report) is gated and its methodology unknown.
