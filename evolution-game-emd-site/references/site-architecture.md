# Extended site architecture (beyond the homepage)

Format for the deliverable: compact tiered list. Each page line carries: URL · title · primary keyword (India vol) · secondaries with vol separated by middots · competitor angle · schema · priority phase. Tag pages that carry numeric game facts with `[LOCKED-DATA]` and pages with legal/prediction exposure with `[COMPLIANCE]`. End with a build order and an internal-linking silo map.

## Tier map used for Ice Fishing (India): adapt volumes per game

**Tier 1: Results silo (build FIRST, KD ~0, ~45–50K/mo combined)**
- `/results/`: `<game> result` (30,000) · result today (4,600) · results (3,400) · game result (1,300) · results today india (1,000) · live result (300). Live-results explainer + "latest results" table with visible last-updated stamp + honest RNG framing. Schema: WebPage + FAQPage. Consolidate results/tracker/stats on ONE page unless the tracker sub-cluster alone clears ~1,500/mo (it did for Ice Fishing: casino score 600 · tracker 400 · casino scores 300 · tracker online 250).
- `/tracker/` (optional spoke): tracker/stats brand terms (tracksino, casino.org). Explain what a tracker shows; ship even a simple widget if possible.
- `/big-win/` (optional spoke): result big win (450) · big win today (300) · highest win (60–80). Emotional/promo page; the maths lives on /rtp/.

**Tier 2: Commercial intent**
- `/real-money/`: real money (750 combined) · gambling game · betting game. Payments table, KYC, 30% tax. [COMPLIANCE]
- `/online-casinos/` (where-to-play): casino (1,300) · where to play (150) · online casino. Criteria-first, one verified partner block (#partner), affiliate CTA. Money page.
- `/demo-online/`: demo (700) · free play · demo apk. Honest: live shows rarely have demo.
- `/download/`: app · apk · download (~950 combined). "No APK needed", fake-APK warning.

**Tier 3: Topical depth / authority**
- `/how-to-play/`: how to play (150) · history (250) · original game (150). HowTo schema.
- `/bonus-rounds/` or `/game-guide/`: wheel (60) · bonus (60) · slot confusion (100+50). [LOCKED-DATA]
- `/rtp/`: RTP, odds, max win, highest multiplier. [LOCKED-DATA] Link target from every page.
- `/evolution-<game>/`: `<game> evolution` (200) · evolution gaming (100). Provider authority; stablemate comparison as a section, not standalone "vs" pages (negligible India volume).
- `/reviews/` or `/<game>-review/`: review (70). First-person experience signals, pros/cons, verdict. Review schema only with a real rating.

**Tier 4: Trust / legal / clarifiers**
- `/is-<game>-real/`: real or fake (250) · real game (90). [COMPLIANCE]
- `/is-<game>-legal/`: legal status in India, Public Gambling Act 1867, state variation (Goa/Sikkim/Meghalaya vs Andhra/Telangana/Tamil Nadu restrictions), Promotion and Regulation of Online Gaming Act 2025, 30% TDS. Build this FIRST as single source of truth and link, don't copy. [COMPLIANCE]
- `/rng-fairness/`: certified RNG + physical wheel + audits. NEVER "provably fair / server seed / client seed" for an Evolution wheel game (that is crash-game wording and factually wrong).
- `/prediction/`: debunk page only. [COMPLIANCE]
- `/strategy/`, `/glossary/`, `/comparisons/`, `/live/`, `/payments/`, `/bonuses/`

**Tier 5: Geo / language (only for the 30–60 page build)**
- `/hindi/` + Hindi mirrors of every guide page (hreflang hi-IN); optional `/bn/ /ta/ /te/ /mr/ /kn/`
- State pages: `/maharashtra/ /karnataka/ /tamil-nadu/ /west-bengal/ /up/ /assam/ /tripura/ /arunachal-pradesh/ /telugu/` etc. Each = legal status in that state + how to play from there + same LOCKED-DATA facts. Keep them 900–1,300 words, distinct intros, no doorway duplication.

**Utility (always, required for YMYL):** `/about-us/ /contact-us/ /responsible-gambling/ /terms-and-conditions/ /privacy-policy/ /cookie-policy/ /disclaimer/ /sitemap/ (html)`

**Redirects (noindex, not in sitemap):** `/play/` and `/login/` → affiliate URL.

## Silo map
```
HOME (hub)
 ├─► /results/ ──► /tracker/, /big-win/, /prediction/
 ├─► /how-to-play/ ──► /bonus-rounds/, /rtp/
 ├─► /demo-online/
 ├─► /real-money/ ──► /payments/, /online-casinos/ (money)
 ├─► /download/
 ├─► /is-<game>-real/ ──► /rng-fairness/, /is-<game>-legal/
 ├─► /evolution-<game>/ ──► /comparisons/
 └─► footer: about, contact, responsible-gambling, terms, privacy, cookies, hindi
```
Rules: every page links up to home + 2–3 siblings; /results/, /online-casinos/ and /play/ CTA from every page; descriptive keyword anchors; prediction/real-or-fake pages link to /responsible-gambling/; homepage keeps prediction/demo/real-or-fake sections short and points to the deep pages.

## Build order by ROI
1. /is-<game>-legal/ (source of truth) + utility pages
2. /results/ (biggest volume, KD 0)
3. /online-casinos/ (money)
4. /demo-online/
5. /how-to-play/ + /rtp/ + /bonus-rounds/
6. /real-money/, /download/
7. /is-<game>-real/, /prediction/, /rng-fairness/
8. /evolution-<game>/, /reviews/, /comparisons/
9. /hindi/ mirrors, then state pages

## Template differences vs a crash game (Tower Rush) build
- Wheel game: results/tracker cluster dominates; no "provably fair"; no auto-cashout/strategy pages.
- Crash game (Galaxsys Tower Rush): app/APK cluster dominates (~40K combined); provably-fair page is correct; add trap-settings / bonus-floor pages (Frozen / Temple / Triple Build); name the real developer (Galaxsys).
