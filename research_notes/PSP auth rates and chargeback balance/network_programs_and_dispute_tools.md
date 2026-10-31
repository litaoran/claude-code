# Card Network Chargeback/Fraud Monitoring Programs and the Dispute-Prevention Ecosystem (as of late Oct 2026)

Source-quality note: The only primary network document I could read in full was Visa's VAMP fact sheet (PDF, "VAMP_external fact sheet_2025 v2", created 14 May 2025). Mastercard's rule bulletins sit behind Mastercard Connect and were not accessible. Mastercard's 2025 State of Chargebacks PDF returned HTTP 403. Most other figures come from acquirer/PSP documentation (Stripe, Checkout.com), which is fairly reliable, or from dispute-vendor blogs (Chargebacks911, Chargeflow, Chargeback Gurus, Ravelin), which have a commercial interest and are less reliable. Conflicts are flagged inline.

## Q1. Visa Acquirer Monitoring Program (VAMP): ratio, thresholds, timeline, fees, regional differences, enumeration, and treatment of RDR/CDRN

### Takeaway
VAMP folds the old VDMP (disputes) and VFMP (fraud) programs into one global, count-based CNP metric: (TC40 fraud reports + TC15 disputes) ÷ settled CNP transactions (TC05). Since 1 Apr 2026 a merchant is "Excessive" at ≥1.5% (150 bps) with ≥1,500 monthly fraud+dispute count in AP, Canada, EU, US and LAC. CEMEA stays at ≥2.2% with ≥150 count and ≥USD 75,000. Acquirers are "Above Standard" at ≥0.5% and "Excessive" at ≥0.7%. A separate enumeration (card-testing) test applies at ≥20% and ≥300,000 enumerated authorizations. Visa's fact sheet publishes no fees. Processors report $8 per counted event for Excessive merchants and $4/$8 for acquirers. Pre-dispute resolutions and CE3.0-qualified TC40s are excluded, "contingent on the timing of the data extract." Sources disagree on whether fraud disputes resolved via RDR/CDRN are excluded.

### Cited Findings
**Formula and scope (primary, Visa)**
- Visa: "The core program metric is a single, count-based ratio (VAMP ratio) that includes key components of fraud and disputes on card-not-present VisaNet transactions (domestic and cross-border)." VAMP Ratio = Count of [Fraud (TC40) + Disputes (TC15)] ÷ Count of Settled Transactions (TC05). The ratio definition is footnoted "Effective 1 June 2025." — [Visa VAMP fact sheet 2025](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Visa: the VAMP ratio "Excludes disputes resolved through pre-dispute solutions, contingent on the timing of the data extract" and "Excludes TC 40 fraud qualified for Compelling Evidence 3.0, contingent on the timing of the data extract." — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Visa consolidated "the existing VAMP, Visa Fraud Monitoring Program, and Visa Dispute Monitoring Program into a single global program." Threshold updates took effect 1 June 2025, and the "Program advisory period ends 30 September 2025." Footnote: "Programs for Brazil, Chile, and India will be announced later." — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)

**Merchant thresholds (primary, Visa)**
- Excessive Merchant thresholds as published: AP, Canada, EU, US ≥220 bps with monthly fraud+dispute count ≥1,500. LAC ≥150 bps with count ≥1,500. CEMEA ≥220 bps with count ≥150 and amount ≥USD 75,000. Footnote 5: "Excessive Merchant threshold reduced to >=150bps in AP, Canada, EU, and U.S. regions on 1 April 2026." — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Visa's merchant thresholds apply "If acquirer is not Above Standard or Excessive." The fact sheet does not say what applies to merchants when the acquirer is flagged. — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Checkout.com's table matches: from 1 June 2025, LAC ≥150 bps and AP/CEMEA/EU/NA ≥220 bps. From 1 April 2026, AP/EU/LAC/NA ≥150 bps and CEMEA ≥220 bps. Enumeration ≥2000 bps globally. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- Conflict on the CEMEA minimum count: Visa and Stripe say ≥150 count plus ≥USD 75,000. Ravelin says "1,550+ cases and $75,000," which looks like a typo. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs); [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)
- Conflict on LAC's start date: Visa and Checkout.com date the LAC 1.5% level to 1 June 2025. Ravelin says "since April 2025." — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)

**Acquirer thresholds**
- Visa: an acquirer portfolio is "Above Standard" if its VAMP ratio is ≥50 bps and "Excessive" if ≥70 bps. Both levels share the minimum monthly fraud+dispute count of ≥1,500 in AP, Canada, EU, US, or ≥150 and ≥USD 75,000 in CEMEA. — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Timing: Ravelin says acquirer thresholds of 0.5–0.7% / >0.7% took effect 1 Jun 2025 and that "above standard" enrollment began 1 Jan 2026. Its table also shows an acquirer "Early warning" band of 0.40–0.49%, and it says there is no early-warning stage for merchants. — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)
- MRC (via Chargeback Gurus, 1 Apr 2026): acquirer "Above standard" at 0.5% is enforced from 1 January, and "Excessive" is 0.7%. — [Merchant Risk Council blog](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2026/stricter-vamp-ratio-thresholds-are-now-in-effect-heres-how-to-stay-compliant)

**Merchant trigger when the acquirer is flagged (conflicting)**
- Stripe lists a merchant "Non-compliant" threshold of VAMP count 5 and ratio 0.5%, alongside the "Excessive" threshold. "Visa assesses fees to merchants that exceed the Excessive threshold and may assess fees to merchants that exceed the Non-Compliant threshold." — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Chargeflow says flagged acquirers can trigger a 0.5% / ≥5-event merchant threshold, citing Braintree and Stripe. — [Chargeflow VAMP guide](https://www.chargeflow.io/blog/vamp-visa-acquirer-monitoring-program)
- Contradicted by Chargebacks911: "fines may apply to every dispute or TC40 involving any merchant with a VAMP ratio above 0.3%." — [Chargebacks911, 1 May 2026](https://chargebacks911.com/visa-acquirer-monitoring-program/)

**Fees, grace period, enforcement**
- Visa's fact sheet contains no fee amounts. — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Chargebacks911 reports, per CNP TC40 or TC15: $4 for an Above-Standard acquirer, $8 for an Excessive acquirer, $8 for an Excessive merchant. Acquirers must submit a remediation plan within 15 calendar days. Acquirers in Europe and AP "are not fined if an unsecured dispute fee applies." — [Chargebacks911](https://chargebacks911.com/visa-acquirer-monitoring-program/)
- Ravelin: merchants pay $8 per CNP dispute (fraud or non-fraud), "subject to change." Acquirers pay $4 (above standard) or $8 (excessive) per dispute across all merchants in the portfolio. — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)
- Chargeflow: Excessive is $8 per counted event and merchants under an Above Standard acquirer pay $4 (citing Braintree, NMI). The page shows no $10 US figure. — [Chargeflow](https://www.chargeflow.io/blog/vamp-visa-acquirer-monitoring-program)
- Grace period: a first-time violation within a rolling 12 months gets a 3-month grace period before enrollment. — [MRC blog](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2026/stricter-vamp-ratio-thresholds-are-now-in-effect-heres-how-to-stay-compliant); [Chargebacks911](https://chargebacks911.com/visa-acquirer-monitoring-program/); [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)
- Enforcement timeline: VDMP/VFMP retired 31 Mar 2025, updated VAMP began 1 Apr 2025, the transitional period ran to 31 Dec 2025, and official enforcement started 1 Oct 2025. — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes); [Chargebacks911](https://chargebacks911.com/visa-acquirer-monitoring-program/) ("VAMP enforcement (fees and penalties) began October 1, 2025"). This matches Visa's "advisory period ends 30 September 2025."

**Superseded thresholds (original announcement, revised in 2025)**
- Chargeback Gurus (13 Mar 2025) reported the original schedule. Initially: acquirer Excessive 0.5%, merchant Excessive 1.5%. For 2026: acquirer Above Standard 0.3%, acquirer Excessive 0.5%, merchant Excessive 0.9%. Fees: acquirers $5 (Above Standard) / $10 (Excessive), Excessive merchants $10 per transaction. — [Chargeback Gurus](https://www.chargebackgurus.com/blog/visa-announces-new-change-to-vamp-rules)
- Visa's v2 fact sheet (May 2025) superseded this schedule: 2.2% then 1.5% for merchants, 0.5% / 0.7% for acquirers. Some sources still repeat the 0.9% figure, e.g. Decta ("drops to 0.9% by January 2026 for high-risk merchants," per search snippet). — [Visa fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf); [Decta](https://www.decta.com/company/media/what-is-vamp-visa-acquirer-monitoring-programme)

**Enumeration (card testing)**
- Visa: Enumeration Ratio = enumerated authorization transactions (approved + declined) ÷ all authorization transactions (approved + declined), threshold ≥2000 bps. Enumeration Transaction Count threshold ≥300,000. — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Stripe: Visa identifies enumerated transactions with "a machine learning model." An account exceeding both criteria goes into "Excessive" enumeration monitoring, and "Visa doesn't assess fines for VAMP enumeration monitoring." Dispute/fraud and enumeration are monitored separately; you enter only the category you exceed. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Enumeration is confirmed via Visa Account Attack Intelligence (VAAI), which Visa says cuts false positives by 85%. — [Chargeback Gurus](https://www.chargebackgurus.com/blog/visa-announces-new-change-to-vamp-rules)

**Counting mechanics**
- Stripe: "The same fraudulent transaction might appear in both the TC40 and TC15 reports. Any transaction that appears in both reports will be counted twice for the VAMP count."
- Stripe: early fraud warnings (TC40s) count in VAMP "regardless of their outcome."
- Stripe: refunds and dispute outcomes do not remove a dispute from monitoring calculations.
- Stripe: "Issuers are required to report possible fraud for a captured payment, even if it gets refunded, but aren't required to report it for a payment authorization." Voiding a suspicious authorization before capture therefore avoids a TC40.
- Stripe: Visa computes ratios within the same calendar month, assigns disputes and fraud reports to the month received, and identifies merchants by statement descriptor plus acquirer. EU volume is aggregated across EU countries.
- Source for all five points above: [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

**Treatment of RDR / CDRN / Ethoca / CE3.0 (conflicting)**
- Visa (May 2025 v2): pre-dispute resolutions are excluded, contingent on extract timing. The fact sheet does not distinguish fraud from non-fraud disputes. — [Visa fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- Chargeback Gurus (13 Mar 2025): on 11 Mar 2025 Visa said fraud-related disputes resolved via RDR or CDRN "will no longer be excluded from the VAMP ratio calculation," while non-fraud disputes resolved that way stay excluded. — [Chargeback Gurus](https://www.chargebackgurus.com/blog/visa-announces-new-change-to-vamp-rules)
- Ravelin (updated Jan 2026): Visa first said TC40s would not be excluded, then reversed. The exclusion now covers "TC15 non-fraud disputes resolved through pre-dispute solutions, 'including but not limited to' RDR." It is no longer limited to Visa tools and names Verifi and Ethoca. — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes)
- Checkout.com: exclusions cover disputes resolved within the same month through Ethoca, Verifi, CDRN, RDR, and CE3.0. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- Chargebacks911: disputes resolved via RDR and CDRN are excluded, and reason code 10.4 disputes resolved with CE3.0 are excluded. The RDR/CDRN exclusion changes apply in all regions except Latin America. — [Chargebacks911](https://chargebacks911.com/visa-acquirer-monitoring-program/)
- MRC/Chargeback Gurus (Apr 2026): RDR disputes are "removed from the VAMP calculation entirely." CDRN/Ethoca refunds are not submitted as chargebacks, but "A TC40 may or may not be filed." — [MRC blog](https://merchantriskcouncil.org/learning/resource-center/member-news/blog/2026/stricter-vamp-ratio-thresholds-are-now-in-effect-heres-how-to-stay-compliant)
- Stripe: "Non-disputed funds that move through a card network's dispute system… as part of Visa's Rapid Dispute Resolution program" do not count as disputes. Disputes resolved via pre-dispute products such as Stripe's dispute prevention are excluded. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

**New in 2026: Visa Merchant Elevated Risk Program (MERP), Asia Pacific**
- Stripe: MERP is effective October 2026 for businesses accepting Visa in AP. Visa evaluates merchants individually, early in their lifecycle, on transaction count/volume, fraud volume/rate, non-fraud dispute volume/rate, and authorization count/decline rate. Visa "doesn't publish the thresholds." Consequences can include non-compliance assessments, backdated fraud disputes (issuers may file past standard deadlines), remediation plans, account closure, and VMSS listing. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Checkout.com gives the exact start date as 9 October 2026 and says MERP works alongside VAMP. Razorpay says only "October 2026." — [Checkout.com support](https://support.checkout.com/hc/en-us/articles/36650358354450-What-is-the-Visa-Merchant-Elevated-Risk-Program); [Razorpay docs](https://razorpay.com/docs/payments/international-payments/visa-merp)
- Visa AP says MERP targets "unusual transaction spikes, higher fraud or dispute ratios, or inconsistent activity patterns." — [Visa Singapore story, 2026](https://www.visa.com.sg/about-visa/stories/2026/driving-fraud-down-in-asia-pacific-a-safer-payments-ecosystem-by-design.html)

**Other Visa program (US only)**
- Visa Secure Excessive Fraud Program: US merchants with domestic 3DS-authenticated fraud (TC40 $) ≥USD 75,000 and a ≥0.9% fraud rate. There are no fines, but the merchant loses the 3DS liability shift until exit. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

### Inferences
- Because the VAMP ratio is count-based and counts a third-party-fraud case twice (TC40 + TC15), a merchant at 0.75% chargebacks with all disputes fraud-related could already be near 1.5% VAMP. Card-testing and true-fraud control therefore matter more than under VDMP, which counted disputes only.
- Taken together, the sources suggest RDR/CDRN can remove the TC15 (dispute) leg from the count but not an issuer-filed TC40. A fraud case resolved pre-dispute may still count once, unless the TC40 qualifies for CE3.0. This reading fits both the Visa and Ravelin wording, but it is my inference. The fact sheet does not say this explicitly.
- Acquirer thresholds (0.5% / 0.7%) are far below the merchant 1.5% threshold. Acquirers/PSPs therefore have a strong incentive to enforce internal merchant limits well below 1.5%. Chargeback Gurus made this point about an earlier draft ("Acquirers may set stricter merchant-level thresholds").
- Exclusions depend on the "timing of the data extract." A pre-dispute resolution that lands in a different month from the TC15 may not be excluded. Checkout.com describes this as a "same month" requirement.

### Gaps
- No official Visa fee schedule was found. The $4/$8 figures are processor- and vendor-reported, and the superseded $5/$10 schedule shows these can change. I found no confirmed region-specific fee (e.g., a US-specific $10).
- The merchant-level trigger when the acquirer is Above Standard/Excessive is unresolved: 0.5% with ≥5 events (Stripe/Braintree) vs. "above 0.3%" (Chargebacks911).
- Whether fraud (TC40) records resolved via RDR/CDRN are excluded remains contested. A Visa Business News or Visa Core Rules citation was not accessible.
- The Brazil, Chile, and India program details ("announced later") were not found.
- I did not re-verify the legacy VDMP/VFMP thresholds from a primary source in this session.

## Q2. Mastercard programs: Excessive Chargeback Program (ECM/HECM), Excessive Fraud Merchant (EFM), acquirer programs, and 2025–2027 changes (GMAP)

### Takeaway
Through late 2026, Mastercard's Excessive Chargeback Program (ECP) is unchanged. ECM is 100–299 chargebacks at a 1.5–2.99% ratio. HECM is ≥300 chargebacks at ≥3%. The ratio is this month's chargebacks divided by the previous month's transactions. Fines escalate from month 2: up to $100k/month for ECM and $200k/month for HECM. EFM targets low-3DS e-commerce merchants with ≥$50k fraud chargebacks and ≥0.5% fraud ratio. In July 2026 Mastercard announced the Global Merchant Audit Program (GMAP), effective 1 Apr 2027, replacing the Acquirer Chargeback Monitoring Program (ACMP). It adds new merchant tiers (HDM/EDM) and acquirer tiers (HDA/EDA), and phases the ECM ratio down to 0.9% by 2031. Sources disagree on whether ECM/HECM/EFM survive alongside GMAP.

### Cited Findings
**ECP: ECM and HECM (current)**
- Stripe: placement requires meeting both chargeback count and chargeback rate. The rate is "the chargeback count for the current month to the total number of captured payments from the preceding month." A chargeback is assigned to the month it is raised. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- ECM: 100–299 chargebacks and a 1.5–2.99% rate. Fines by month: month 1 $0; months 2–3 $1,000; 4–6 $5,000; 7–11 $25,000; 12–18 $50,000; 19+ $100,000. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- HECM: ≥300 chargebacks and ≥3% rate. Fines: month 1 $0; month 2 $1,000; month 3 $2,000; 4–6 $10,000; 7–11 $50,000; 12–18 $100,000; 19+ $200,000. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- From month 4, an "issuer recovery assessment" adds $5 per chargeback over 300. Stripe's example: $5,000 + (400−300)×$5 = $5,500. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Exit requires staying below the threshold for 3 consecutive months. A HECM merchant below HECM but still at ECM levels drops to ECM. Mastercard counts chargebacks "regardless of whether it was hidden due to a refund, regardless of liability shift… and regardless of its outcome." — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Conflict on the trigger window: secondary sources variously say the thresholds must be met for 2 (not necessarily consecutive) months, in a single month, or for two consecutive months. Stripe describes monthly evaluation with fines from month two. — [Chargeflow](https://www.chargeflow.io/blog/avoid-mastercard-chargeback-monitoring-programs); [Chargeback Help](https://chargebackhelp.com/mastercard-excessive-chargeback-program-ecm-and-hecm-explained/); [Chargeback Gurus](https://www.chargebackgurus.com/blog/mastercard-excessive-chargeback-program)

**EFM: Excessive Fraud Merchant**
- Checkout.com: placement uses the previous calendar month's data and requires all of the following: at least 1,000 Mastercard sales; at least USD/EUR 50,000 in fraud chargebacks (reason code 4837); a fraud chargeback-to-sales ratio ≥0.5% (50 bps); and 3DS (including Data Only) or DSRP share below 10% of clearing volume in non-regulated countries or below 50% in regulated countries. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- Stripe adds: reason codes 4837 or 4863 count. Australia uses lower thresholds of $15,000 and 0.20%. EFM does not apply in Germany, India, or Switzerland. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- Checkout.com adds Liechtenstein and some territories to the ACMP exclusion list. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- EFM fines: month 1 $0; month 2 $500; month 3 $1,000; 4–6 $5,000; 7–11 $25,000; 12–18 $50,000; 19+ $100,000. Exit takes 3 consecutive compliant months. Exiting early by processing zero sales triggers retroactive assessments. If a merchant is in both EFM and ECM in the same month, only EFM assessments apply. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md); [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- A merchant may request a one-time suspension of an assessed fine during an open case. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

**Other Mastercard programs**
- Scam Merchant Monitoring Program (SMMP), global CNP except Jordan. For new merchants (under 6 months of history, more than 500 transactions/month), acquirers must investigate within 72 hours if refunds plus chargebacks exceed 5% of purchases over a rolling 30 days, or if ≥2 issuers report fraud type 56 or scam chargebacks. For all merchants, the trigger is an approval-rate drop of ≥50 percentage points or a rate below 30% over 72 hours. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)

**2026 announcement: GMAP (effective 1 April 2027)**
- Chargebacks911 (12 Aug 2026): Mastercard announced GMAP in July 2026, effective 1 Apr 2027, replacing ACMP. Monitoring is at merchant (MID) and acquirer (ICA) level. GMAP "combines confirmed fraud, including fraud that doesn't result in a chargeback, with non-fraud chargebacks." — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- High Dispute Merchant (HDM): ≥5 cleared transactions, ≥$5,000 in combined chargebacks, and a ratio ≥5%. Assessments: months 1–6 $0; 7–11 $5,000; 12–18 $10,000; 19+ $25,000. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- Excessive Dispute Merchant (EDM): ≥5 cleared transactions, ≥$10,000, and a ratio ≥50%. Assessments: month 1 $5,000; month 2 $25,000; 3–11 $100,000; 12–18 $200,000; 19+ $300,000. After 2 months, the merchant is liable for fraud chargebacks covering 3 months before and 6 months after identification. Mastercard publishes a monthly EDM list, and issuers may use reason code 4849 for 100% of the amount. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- High Dispute Acquirer (HDA): ≥1,500 chargebacks and a ratio ≥0.5%. Assessments: months 1–11 $0; 12–18 $25,000; 19+ $50,000. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- Excessive Dispute Acquirer (EDA): ≥1,500 transactions, ≥1,500 chargebacks, and a ratio ≥0.7%. Assessments: months 1–2 $0; 3–6 $10,000; 7–11 $25,000; 12–18 $50,000; 19+ $100,000. At 12+ months a Franchise Management Program review is required, with possible license suspension beyond 19 months. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- Key dates: 4 Jan 2027, Mastercom Acquirer Collaboration decommissioned in US/Canada. 1 Apr 2027, GMAP replaces ACMP, revised QMAP standards take effect, and sub-merchant ID monitoring starts for ECM/HECM/EFM (PayFac sub-merchants evaluated independently). 30 May 2027, GMAP assessments begin. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- ECM ratio phase-down, all with the 100-chargeback minimum: 1.5% through 2028, 1.3% from 1 Jan 2029, 1.1% from 1 Jan 2030, 0.9% from 1 Jan 2031. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)
- The phase-down timing conflicts in search snippets. Some say 2029–2031, one says "between 2027 and 2031," and another says ECM criteria are unchanged for 2027–2028. — [Chargeflow GMAP](https://www.chargeflow.io/blog/mastercard-global-merchant-audit-program-gmap); [payabl](https://payabl.com/news/mastercard-gmap-what-merchants-need-to-do-before-april-2027); [Chargeback Help](https://chargebackhelp.com/gmap-and-what-merchants-should-expect-in-2027/)
- Bulletin reference GLB 14127.1, published 28 July 2026, per search-surfaced vendor summaries. — [Slyce360](https://www.slyce360.com/mastercard-gmap-explained-what-acquirers-need-to-know-before-april-2027/); [Chargemate](https://www.chargemate.tech/articles/mastercard-gmap-guide-2027)
- Conflict on scope: Chargebacks911 says ECM, HECM and EFM "will operate side-by-side with GMAP." Other summaries say GMAP "consolidates the existing EFM, ECM, and HECM categories into a single program." — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/) vs. vendor summaries surfaced in search ([Chargeflow GMAP](https://www.chargeflow.io/blog/mastercard-global-merchant-audit-program-gmap); [y.uno](https://y.uno/en/blog/visa-vamp-and-mastercard-gmap-how-enterprise-merchants-should-audit-their-fraud-and-dispute-expo))

### Inferences
- From 2027, Mastercard's measurement moves toward Visa's model: confirmed fraud counted even without a chargeback, plus disputes. Later, ECM converges to 0.9%. Merchants should plan for ~0.9% as the long-run ceiling on both networks for disputes alone.
- The EFM 3DS carve-out (≥10% / ≥50% 3DS share) is effectively a policy lever: routing even a modest share of Mastercard e-commerce traffic through 3DS takes a merchant out of EFM scope.
- Sub-merchant-level monitoring from April 2027 removes the "hide inside a PayFac aggregate MID" effect for marketplace and platform sellers.

### Gaps
- I could not access the primary Mastercard GMAP bulletin (GLB 14127.1), so the GMAP tier thresholds and assessments rest on one vendor's (Chargebacks911) reading. The EDM 50% ratio figure in particular should be confirmed.
- I found no confirmed treatment of Ethoca-resolved disputes, or of fraud reported to Mastercard (SAFE/FRM) without a chargeback, under GMAP.
- The exact ECM/HECM trigger window (single month vs. two months) is not confirmed from Mastercard primary text.

## Q3. American Express, Discover, and other regional schemes (brief)

### Takeaway
Amex and Discover do not publish Visa/Mastercard-style tiered programs. Secondary sources commonly put Amex's excessive-chargeback line at ~1%, with per-chargeback fees, plus a separate Fraud Full Recourse Program at 0.90%/$25k and 1.80%/$50k. Discover is commonly cited at ~1% or >100 chargebacks/month. Domestic schemes such as Cartes Bancaires (France) and AusPayNet (Australia) run their own fraud and dispute programs.

### Cited Findings
- Amex: several secondary sources say a chargeback ratio above 1% for three consecutive months is "excessive," with a $25 fee per chargeback over the 1% threshold. BlueSnap lists added minimums of >10 net chargebacks and >50 net transactions per month. One source gives different figures: $5 per disputed charge under the Immediate Chargeback Program and $15 otherwise. — [Justt](https://justt.ai/blog/how-american-express-and-discover-chargebacks-differ/); [BlueSnap](https://support.bluesnap.com/docs/chargeback-monitoring-programs); [Chargeback Gurus](https://www.chargebackgurus.com/blog/american-express-chargeback-fees)
- Amex Fraud Full Recourse Program: low tier at a 0.90% fraud ratio with ≥$25,000 fraud; high tier at 1.80% with ≥$50,000. — [Chargeback Gurus](https://www.chargebackgurus.com/blog/amex-excessive-chargeback-fees-and-fraud-full-recourse-program)
- Discover: generally considers >1% or >100 chargebacks/month excessive, with $25 per chargeback above the 100/month limit. Discover does not publish detailed tiers. — [Justt](https://justt.ai/blog/how-american-express-and-discover-chargebacks-differ/)
- Cartes Bancaires Fraud Program: entry at a >0.50% fraud-to-sales ratio and ≥€20,000 fraud for 4 consecutive months. Fine = 50 × fraud ratio × fraud amount, capped at €50,000. Exit at <0.50% for 6 months. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- Cartes Bancaires Disputes Program: entry at a >2% dispute-to-sales count ratio and 200 disputes for 4 consecutive months. Fine of €50 per dispute (€35 goes to the issuer). Exit at <1% and <100 disputes for 6 consecutive months. — [Checkout.com docs](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- AusPayNet CNP Fraud Monitoring Program (quarterly, AU only): triggered by fraud chargebacks >AUD 50,000 and a fraud-to-sales value ratio ≥0.20%, excluding card-present and 3DS-authenticated transactions. Escalation: SCA on high-risk CNP, then SCA on all CNP by quarter 3, then possible off-boarding from quarter 4. — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

### Inferences
- For a multi-network merchant, Visa VAMP (1.5% including TC40 fraud) and Mastercard ECM (1.5% chargebacks only, previous-month denominator) are the binding constraints. Amex's ~1% guideline may bind first for Amex-heavy merchants, but enforcement is less formalized.

### Gaps
- No primary Amex or Discover documentation was obtained. All Amex/Discover figures are secondary and partly conflicting, and their recency (2025–2026) is unverified.

## Q4. Dispute prevention and resolution tools: how they work, cost, deflection, and effect on counted ratios

### Takeaway
Visa-side tools are RDR (rules-based automatic pre-dispute refund), Verifi CDRN (alerts), Order Insight (sharing order data with issuers), and CE 3.0 (first-party-misuse rebuttal for reason code 10.4, usable pre-dispute via Order Insight). Mastercard-side tools are Ethoca Alerts, Consumer Clarity, and the First-Party Trust program. Alerts and RDR typically cost ~$15–$40 per alert or case, set by resellers rather than the networks. Post-dispute vendors such as Chargeflow, Justt, Chargebacks911 and Midigator mostly charge contingency fees (~25–35% of recovered funds) or subscriptions. Representment wins do not reduce network ratios. Only pre-dispute deflection (and CE3.0-qualified TC40s for Visa) removes items from the count, and for fraud cases a TC40 may still count.

### Cited Findings
**How each tool affects the counted ratio**
- Monitoring programs "don't consider dispute outcomes… They're also more interested in how successfully you prevent disputes than in whether you win them." — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)
- CE 3.0 via Order Insight (pre-dispute): "Visa pre-selects up to five qualifying prior purchases and sends them as Order Insight inquiries." If the criteria are met, the dispute is blocked and liability stays with the issuer; it "does not affect fraud or chargeback ratios," and Order Insight enrollment is required. CE 3.0 in representment (post-dispute, via VROL): the chargeback fee still applies and the dispute "counts toward the chargeback rate." — [Chargebacks911, 20 Dec 2025](https://chargebacks911.com/prevent-chargebacks/prevent-visa-disputes/visa-compelling-evidence-3-0/)
- CE3.0-qualified TC40 fraud is excluded from the VAMP ratio, contingent on extract timing. — [Visa VAMP fact sheet](https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf)
- RDR, CDRN, and Ethoca exclusions from VAMP are conflicting by fraud vs. non-fraud and by region. See Q1. — [Ravelin](https://www.ravelin.com/blog/visa-vamp-changes-chargeback-disputes); [Chargeback Gurus](https://www.chargebackgurus.com/blog/visa-announces-new-change-to-vamp-rules); [Checkout.com](https://www.checkout.com/docs/business-operations/manage-disputes/scheme-monitoring-programs.md)
- Stripe recommends Ethoca and Verifi for subscription merchants: "an alert is raised when a chargeback is about to be initiated, allowing the user an opportunity to refund." — [Stripe docs](https://docs.stripe.com/disputes/monitoring-programs)

**CE 3.0 rules**
- CE 3.0 applies only to Visa reason code 10.4 (card-absent fraud), not to "item not received" or "not as described" disputes. — [Chargebacks911](https://chargebacks911.com/prevent-chargebacks/prevent-visa-disputes/visa-compelling-evidence-3-0/); [cside](https://cside.com/blog/compelling-evidence-3-requirements-data-points)
- It requires two prior undisputed, non-fraud-reported transactions on the same credential, processed 120–365 days before the disputed transaction. At least 2 of 4 data elements (user/account ID, delivery address, device ID/fingerprint, IP address) must match, and one must be IP address or device ID. Subscription merchants may use the undisputed initial subscription transaction. — [Chargebacks911](https://chargebacks911.com/prevent-chargebacks/prevent-visa-disputes/visa-compelling-evidence-3-0/)
- Window discrepancy: Stripe's API documentation reportedly says 120–364 days, while Visa says ≤365 days. — [cside](https://cside.com/blog/compelling-evidence-3-requirements-data-points)
- Reported but unverified: for 10.4 disputes processed on or after 24 Oct 2026, the two prior transactions "may have taken place at one or more merchants." This would let networks match history across merchants. — [cside (search snippet)](https://cside.com/blog/compelling-evidence-3-requirements-data-points); see also [Chargeflow CE3.0 "2026 changes"](https://www.chargeflow.io/blog/visa-compelling-evidence-3-0-explained)

**Mastercard-side tools**
- Mastercard says merchants and issuers estimate about 20% of disputes are linked to first-party fraud. It positions Ethoca (Alerts and Consumer Clarity) for first-party fraud prevention. (Search snippet; the page returned HTTP 403 on fetch.) — [Mastercard Insights 2026](https://www.mastercard.com/us/en/news-and-trends/Insights/2026/how-ethoca-helps-prevent-first-party-fraud-and-reduce-chargebacks.html)
- Mastercard extended its First-Party Trust program to Europe. (Headline only; details not retrieved.) — [The Paypers](https://thepaypers.com/fraud-and-fincrime/news/mastercard-extends-first-party-trust-programme-to-europe); [CardRates](https://www.cardrates.com/news/mastercard-takes-first-party-trust-global-to-fight-fraud/)

**Costs (vendor- or reseller-reported; not network-fixed)**
- Chargeback.io (reseller) lists Ethoca $29 per alert and RDR and CDRN $15 each for US transactions. RDR takes a few business days to activate, and disputes filed before activation get no alert. — [Chargeback.io](https://www.chargeback.io/blog/rdr-vs-cdrn-vs-ethoca)
- Other guides cite ~$15 per RDR/CDRN alert and $24–$29 per Ethoca alert, with some resellers quoting $40. Others cite $20–40 per alert for Ethoca/CDRN and $15–25 per resolved RDR case. Verifi does not publish standardized pricing. — [paymentsandrisk](https://paymentsandrisk.com/docs/chargebacks/prevention/chargeback-alert-pricing/); [BeastInsights](https://beastinsights.com/blog/verifi-vs-ethoca-alerts); [Tagada](https://www.tagada.io/payments/chargeback-alerts)
- Another vendor page puts RDR at $20–30 per dispute resolved. — [Tagada](https://www.tagada.io/payments/chargeback-alerts); [Redo](https://redo.com/resources/articles/chargebacks/rdr-vs-cdrn)
- The same transaction can trigger both an Ethoca and a Verifi alert, which means paying twice. Vendors advise against double-enrolling. — [Aurai](https://aurai.dev/blog/ethoca-verifi-alerts-economics); [Chargemate](https://www.chargemate.tech/articles/ethoca-alerts-vs-verifi-rdr)
- Chargeflow (own pricing): Automation at 25% of recovered chargebacks; Alerts at $29 per deflected chargeback; Prevent at $0.40 per scanned transaction (one July 2026 review saw $0.20); no contracts or minimums. — [Redo review of Chargeflow pricing](https://redo.com/resources/articles/comparisons/chargeflow-pricing)
- Competitor claims: Justt charges 35% of recovered revenue, according to a competitor (Chargeflow). Another page says Justt quotes enterprises privately. Chargebacks911 "starts at $1,000+/month" with a 2-year minimum, per Chargeflow's comparison. — [Chargeflow vs Justt](https://www.chargeflow.io/chargeflow-vs-justt); [Chargeback.io Justt alternatives](https://chargeback.io/blog/best-justt-alternatives); [Chargeflow vs Chargebacks911](https://www.chargeflow.io/blog/chargeflow-vs-chargebacks911-which-chargeback-solution-for-your-business)
- Midigator ("an Equifax Company") offers custom pricing, and users pay only for disputes won on their behalf. — [TrustRadius](https://trustradius.com/compare-products/chargeflow-vs-midigator)

**Deflection rates**
- I found no network-published deflection rates. In chargeback.io's own dataset, Verifi produced 57.9% of alerts and Ethoca 42.1%, with one case study showing an 83% drop in dispute rate. These are vendor-reported. — [Chargeback.io (search summary)](https://www.chargeback.io/blog/alert-based-prevention)
- One analysis puts alert break-even at roughly $12–$20 per alert and says RDR at $8–$15 is "almost always net-positive." This is illustrative and model-dependent. — [Aurai](https://aurai.dev/blog/ethoca-verifi-alerts-economics)

### Inferences
- In network-ratio terms, ranked from most to least protective: (1) blocking fraud before capture, which produces no TC40 (Stripe); (2) CE3.0 via Order Insight pre-dispute, which removes both the TC15 and the TC40; (3) RDR/CDRN/Ethoca refunds, which remove the TC15 (for non-fraud at least) but may leave a TC40; (4) post-dispute representment, which recovers money but does not lower the ratio.
- Alert fees of $15–$40 plus the refunded amount are worth paying mainly when a merchant is near a threshold, or when ticket sizes exceed fees plus expected representment losses. Low-ticket merchants far below thresholds may lose money on alerts.
- Contingency-fee vendors (25–35%) only touch post-dispute recovery, so they do nothing for VAMP/ECM standing unless they also resell alerts or RDR.

### Gaps
- I found no Visa- or Verifi-published RDR/Order Insight deflection rates or list prices, and no independent data on Ethoca Consumer Clarity or First-Party Trust effectiveness.
- I found no pricing or product details for CAVU, or for Chargebacks911's current pricing (its pricing URL reportedly 404'd in July 2026).
- The 24 Oct 2026 CE3.0 cross-merchant change is unconfirmed by Visa primary documentation.

## Q5. Industry benchmarks: chargeback rates by vertical, first-party/friendly fraud share, and representment win rates

### Takeaway
Benchmarks are weak and vendor-sourced. Typical all-industry chargeback rates are quoted at ~0.26–0.6%. Travel is quoted ~0.9%, SaaS ~0.66%, and gambling ~3.5%. Global chargeback volume is ~261M (2025), forecast at 324M by 2028 (Mastercard/Datos). Estimates of the first-party fraud share vary widely by definition: ~20–21% of chargebacks (Mastercard) vs. merchant estimates of ~44% (Chargebacks911). About 45% of 2024 chargebacks were fraud of either type (Mastercard). Merchants win roughly 44–50% of representments, but net recovery is only ~11% of all chargebacks (Chargebacks911).

### Cited Findings
**Volumes and fraud share (Mastercard/Datos)**
- Mastercard/Datos 2025 forecasts 261M chargebacks in 2025 and 324M in 2028. A Mastercard 2026 citation says 334M by 2028. (Search summaries; the primary PDF was inaccessible.) — [Mastercard 2025 State of Chargebacks (PDF)](https://www.mastercard.com/content/dam/mccom/shared/news-and-trends/insights/2025/2025-global-chargebacks-outlook/pdf/2025-state-of-chargebacks-report.pdf); [Chargeflow stats](https://www.chargeflow.io/blog/chargeback-statistics-trends-costs-solutions)
- 45% of chargebacks in 2024 were either first-party or third-party fraud (Mastercard). — [The Fintech Times](https://thefintechtimes.com/chargebacks-have-a-bad-reputation-for-a-reason-mastercards-reveals-45-in-2024-were-fraudulent/)
- Merchants classed ~21% of chargeback volume as first-party fraud in the 2025 study. Mastercard's 2026 material says ~20% of disputes are linked to first-party fraud. — [Chargeflow stats](https://www.chargeflow.io/blog/chargeback-statistics-trends-costs-solutions); [Mastercard Insights 2026](https://www.mastercard.com/us/en/news-and-trends/Insights/2026/how-ethoca-helps-prevent-first-party-fraud-and-reduce-chargebacks.html)
- Chargebacks will cost merchants $42B globally by 2028. — [CardRates](https://www.cardrates.com/news/mastercard-takes-first-party-trust-global-to-fight-fraud/)
- Brazil shows the highest increase in first-party fraud (truncated snippet). — [Mastercard 2025 report](https://www.mastercard.com/content/dam/mccom/shared/news-and-trends/insights/2025/2025-global-chargebacks-outlook/pdf/2025-state-of-chargebacks-report.pdf)
- Mastercard/Datos: merchants win an average of 50% of representments (secondary citation). — [Chargebacks911 stats](https://chargebacks911.com/chargeback-stats/)

**Chargebacks911 2026 Field Report and related figures**
- Merchants estimate friendly fraud at 43.8% of their chargebacks, and 74% of merchants reported more friendly-fraud chargebacks in 2024.
- Merchants win 43.8% of represented chargebacks but net recovery is only 10.7%. The page itself is internally inconsistent: 44.6% vs 43.8% win rate, and 74% vs 83.4%.
- Global chargeback volume rose from 238M (2023) to 337M (2026), +41%, attributed to Mastercard.
- The average cardholder filed 5.1 chargebacks in 2025, averaging $84 each.
- Source for the four points above: [Chargebacks911 chargeback stats](https://chargebacks911.com/chargeback-stats/)

**Other industry reports**
- 80% of chargebacks are fraud-related (first- plus third-party), per Cybersource's 2024 report as cited by Chargebacks911. — [Chargebacks911 stats](https://chargebacks911.com/chargeback-stats/); [Cybersource 2024 report](https://www.cybersource.com/content/dam/documents/campaign/fraud-report/global-fraud-report-2024.pdf)
- Each $1 of fraud costs US merchants $5.13 (LexisNexis True Cost of Fraud 2026, cited). — [Chargebacks911 stats](https://chargebacks911.com/chargeback-stats/)
- Visa Acceptance/MRC 2025 report: MRC members' dispute win rates are nearly 2× those of non-MRC enterprises (search snippet). — [Visa Acceptance 2025 Global eCommerce Payments & Fraud Report](https://www.visaacceptance.com/content/dam/documents/campaign/fraud-report/global-fraud-report-2025.pdf)
- Secondary sources attribute two different first-party figures to the 2025 report: first-party misuse at ~20% of fraudulent disputes (up to 30% for high-volume online merchants), and 36% of all fraud cases (up from 15% in 2023). The denominators differ, so these are not comparable. — [Visa Acceptance 2025 report](https://www.visaacceptance.com/content/dam/documents/campaign/fraud-report/global-fraud-report-2025.pdf); [Redo stats roundup](https://redo.com/resources/articles/chargebacks/chargeback-statistics)

**Rates by vertical (low reliability)**
- Search-surfaced vendor roundups give: overall ~0.60%; Sift data showing an average of 0.26% by Q3 2025 (+53% vs Q1 2025); travel/hospitality 0.89%; software/SaaS 0.66%; e-commerce ~0.5%; gambling/sports betting 3.5%; one unverified subscription figure of 1.85%. I could not verify which page originated each figure. — [Chargeflow stats](https://www.chargeflow.io/blog/chargeback-statistics-trends-costs-solutions); [PayCompass by industry](https://paycompass.com/blog/chargeback-rates-by-industry/); [ClearlyPayments](https://www.clearlypayments.com/blog/chargeback-rate-by-industry-and-business-type/); [justpricing](https://justpricing.com/chargeback-statistics)
- E-commerce CNP chargeback rates average 0.6–1% (PayKings, cited). — [Chargebacks911 stats](https://chargebacks911.com/chargeback-stats/)
- Mastercard 2025 research shows the highest average chargeback value in travel/hospitality, at $120. — [Mastercard B2B blog](https://b2b.mastercard.com/news-and-insights/blog/what-s-the-true-cost-of-a-chargeback-in-2025)

### Inferences
- The gap between ~20% (Mastercard) and ~44% (merchant self-estimates) for first-party fraud likely comes from definitions and incentives. Merchants tend to classify unrecognized or unauthorized claims as friendly fraud, while networks count confirmed first-party misuse.
- A ~44–50% representment win rate translating into ~11% net recovery means representment alone cannot fix a ratio problem. Prevention and deflection economics dominate.

### Gaps
- No authoritative, network-published chargeback-rate-by-vertical benchmark exists. All vertical figures are vendor-compiled with unclear methodology.
- The primary Mastercard 2025 report could not be read (HTTP 403), so its first-party share and win-rate figures are secondhand.

## Q6. Consequences of exceeding thresholds: fines, MATCH/VMSS, acquirer termination, and high-risk MCC registration (VIRP)

### Takeaway
Breaches escalate from per-item VAMP fees and monthly Mastercard fines (up to $100k–$300k/month) to acquirer remediation demands, reserves, and termination. Termination can lead to a 5-year MATCH (Mastercard) or VMSS (Visa) listing. MATCH code 04 is triggered at a >1% chargeback ratio with ≥$5k in a month. VMSS code 22 is ≥1,000 disputes at a 1.8% ratio. Note that MATCH reason code 12 is PCI DSS non-compliance, not excessive chargebacks. High-risk verticals must also register under the Visa Integrity Risk Program (VIRP): Tier I MCCs 5967, 7273, 5122, 5912, 7995; Tier II 6012, 6051, 4816, 5816. Reported costs are $950 per merchant registration plus per-transaction integrity fees.

### Cited Findings
**MATCH and VMSS (terminated merchant files)**
- Acquirers must screen applicants against MATCH and VMSS. "Listings remain active for 5 years," and "Only the specific acquiring bank that initiated the listing can request a removal." — [Stripe MATCH docs](https://docs.stripe.com/disputes/match)
- MATCH quantitative codes. Code 04 Excessive Chargebacks: monthly Mastercard chargebacks >1% of monthly sales transactions and ≥USD 5,000, both in the same month, with no minimum chargeback count. Code 05 Excessive Fraud: fraud-to-sales dollar volume ≥8%, ≥10 fraud transactions, and ≥USD 5,000 in the same calendar month. Winning chargebacks later does not change eligibility. A listing must be added within 1 business day. — [Stripe MATCH docs](https://docs.stripe.com/disputes/match)
- MATCH qualitative codes include 01 ADC, 02 CPP, 03 Laundering, 07 Fraud Conviction, 08 Questionable Merchant Audit Program, 09 Bankruptcy, 10 Violation of Standards, 11 Collusion, 12 PCI DSS Non-Compliance (removable once compliant), 13 Illegal Transactions, and 14 Identity Theft. — [Stripe MATCH docs](https://docs.stripe.com/disputes/match)
- VMSS quantitative codes. Code 21 Excessive Fraud: USD 250,000 fraud and 1.8% (180 bps) fraud-to-sales amount in any single month, without adequate remediation. Code 22 Excessive Disputes: 1,000 disputes and a 1.8% dispute-to-sales ratio in any single month. Code 25 covers termination after identification in a Visa risk compliance program without adequate remediation. Listings last 5 years. — [Stripe MATCH docs](https://docs.stripe.com/disputes/match)
- Failure to comply with program requirements "can result in the network refusing to process further payments to you." — [Stripe monitoring docs](https://docs.stripe.com/disputes/monitoring-programs)
- MERP (Visa AP, Oct 2026) consequences include possible VMSS listing and backdated fraud disputes. — [Stripe monitoring docs](https://docs.stripe.com/disputes/monitoring-programs)
- GMAP EDM (Mastercard, 2027) consequences include fraud-chargeback liability windows and public listing to issuers. — [Chargebacks911 GMAP](https://chargebacks911.com/global-merchant-audit-program-gmap/)

**Visa Integrity Risk Program (VIRP), high-integrity-risk MCCs**
- VIRP took effect April 2024, replacing the Visa Global Brand Protection Program.
  - Tier I: 5967 (adult/inbound teleservices), 7273 (dating), 5122 and 5912 (online pharmacy), 7995 (gambling).
  - Tier II: 6012 and 6051 (crypto), 4816 (cyberlockers), 5816 (skill gaming).
  - Tier III: 5993 (tobacco), 5966 (telemarketing), 5968 (negative-option billing).
  - Requirements include content moderation and age verification.
  - Source: [MONA Payment Solutions, 19 Feb 2026](https://monasolutions.com/2026/02/19/what-high-risk-merchants-must-know-about-the-visa-integrity-risk-program-virp/)
- Fees (secondary): per-merchant registration fee raised from $500 to $950. Acquirer non-refundable application fee of USD 100,000 (Tier 1) or USD 25,000 (Tier 2), plus annual renewal. Integrity Risk Fee of $0.10 per transaction + 10 bps of volume, with one source listing $0.02 + 10 bps for Europe and other regions. — [Segpay](https://segpay.com/blog/understanding-visas-new-pricing-high-risk-tiers/); [Host Merchant Services](https://hostmerchantservices.com/2024/04/visa-high-risk-fee-raised/); [G2 Risk Solutions](https://g2risksolutions.com/resources/blog/visa-integrity-risk-program-european-pricing-changes/); [PaymentCloud](https://paymentcloudinc.com/blog/visa-integrity-risk-program-high-risk-merchants-guide/)

### Inferences
- A merchant does not need to be in a Visa or Mastercard program to be MATCH-listed. A >1% Mastercard chargeback ratio with ≥$5k in a single month plus termination is enough, which is a much lower bar than ECM (1.5% and 100 chargebacks). Acquirer risk appetite is therefore usually set near ~0.75–1%, not at the network program lines.
- The VMSS code 21/22 figures (1.8%, 1,000 disputes, $250k fraud) look like the legacy VDMP/VFMP "excessive" levels carried forward. This is an inference that I did not verify.

### Gaps
- I did not retrieve Mastercard's high-risk merchant registration program (Specialty Merchant Registration / BRAM) fees and MCC list for 2026. A PaymentCloud PDF titled "mastercard high risk registration 2026" exists but was not fetched.
- Current (2026) VIRP fee levels are from secondary sources dated 2023–2024 and may have changed. I found no Visa primary VIRP fee schedule.
- Acquirer-specific consequences (reserves, rolling holds, termination thresholds) vary by PSP and are not network-mandated. I found no systematic data on them.
