# Homepage outline format and the icefishing-game.co blueprint

## Output format for an outline deliverable
Always deliver in this order (plain text / markdown file, no em dashes):

1. **SERP intelligence**: who ranks (EMD cluster vs operators), the content pattern every ranker shares, the 3–5 gaps to exploit.
2. **Voice / tone of speech**: register, person, reading level, sentence length, must-convey, avoid, localisation.
3. **Primary + secondary keyword map**: table with keyword, India volume, KD, placement (H1 / H2 name / FAQ / body).
4. **Semantic / entity terms**: provider, mechanics, bonus rounds, payouts, India money, online-play context, stablemates.
5. **Section-by-section structure**: H1, each H2 with its H3s, target keywords, word count, image slot.
6. **Images**: count (homepage: 8–10 SVG/WebP), keyword filenames, alt text.
7. **Schema stack**: see build-spec.
8. **Meta title and description**: title ≤ 60 chars with primary keyword first; description 158 chars, keyword first, year included, no "learn / discover / explained".
9. **Internal links out** and a one-paragraph note on what the homepage keeps short so silo pages don't cannibalise.

## The live icefishing-game.co homepage (copy this structure)

Title: `Ice Fishing Game Live Results & RTP Tracker (India)`
H1: `Ice Fishing Game: Live Results, Rules and Where to Play in India`
Eyebrow above H1: `18+ · Informational guide · Live results · INR / UPI`
Lead paragraph (60–80 words): primary keyword in first sentence, provider, wheel spec, result intent, INR/UPI.
CTA row: `Play <Game> →` (to /play/) + ghost `View Live Results` (#results)
Result strip (4 chips): Provider · Top RTP · Max win · Min bet
Hero SVG: live wheel illustration with "LIVE" badge and 5 sample results (labelled historical, not prediction)
Intro paragraph: what it is NOT (not a simulator, not a slot, not skill) + what it IS
**Spec grid (10 cells):** Provider, Release, Top RTP, Max win, Min bet, Wheel, Bonus rounds, Round time, Devices, Download

Then H2s in this order:
1. `<Game> Live Results and Stats Today` (#results): results cluster; sample results table (Time / Result / Type / Multiplier / Notes); `call-info` callout saying sample data, not a live feed; paragraph on "history is not prediction"; CTA row
2. `What Is the <Game> Game?`: wheel layout SVG with segment counts; definition sentence 35–45 words (snippet bait); stablemate family mention; "not an unrelated fishing/arcade game" clarifier
3. `How to Play <Game> Game`: step SVG; 7 numbered steps (`ol.steps`): choose licensed casino → register + KYC → deposit (UPI/Paytm/PhonePe) → open live lobby → choose bet → watch spin → review and stop
4. `Bonus Rounds: <names>`: bonus SVG; one H3 per bonus tier with frequency, payout ceiling, stake-sizing advice
5. `RTP, Odds and Payouts`: RTP bar SVG; table Bet / Segments / Probability / Base payout / Max with multiplier / RTP; house-edge paragraph
6. `Is the <Game> Game Real or Fake?`: real = Evolution via licensed platform; fake signs list (guaranteed income, predictor sales, Telegram admins, no KYC)
7. `Can You Predict <Game> Results?`: "No." `do2` grid: `do-ok` "A result page may show" vs `do-no` "It should not claim"
8. `<Game> Game Demo: Is It Available?`: honest answer for live shows; observation advice; fake demo APK warning
9. `Real Money Play and Payments in India`: payments SVG; Method / Why it matters / Best for table; KYC paragraph; checklist bullets; H3 `Tax on Winnings` (30% Sec 115BBJ, TDS 194BA)
10. `<Game> Game App and Download`: no APK needed, browser/casino app, fake APK risk
11. `Where to Play <Game> Game in India`: 9 selection criteria bullets; CTA `Compare Licensed <Game> Platforms →` to /online-casinos/#partner
12. `Promo and Offer Types`: 7 bonus types with T&C caveats
13. `Tips for Playing <Game> Game`: session plan table (Learner / Balanced / High volatility) + don'ts
14. `<Game> vs Crazy Time, Funky Time and Dream Catcher`: comparison paragraphs; CTA row
15. `Frequently Asked Questions`: 12 `details` accordions (FAQPage schema mirrors these exactly)
16. `Responsible Gaming`: paragraph + `call-rg` callout with KIRAN 1800-599-0019 + `call-info` footer trust notice

After main: `aside.author` (Reviewed by the Editorial Team, method, Updated <Month Year>), `sticky-cta` bar, footer (brand blurb, Game guides, About & legal, Language columns, affiliate disclaimer, 18+ line).

Word count target for the homepage: 3,000–3,800 words. Inner guide pages: 1,800–2,600. Policy pages: 1,200–2,000.

## Inner page H2 skeletons (live site)
- **/how-to-play/**: What You Need Before Playing · Play in Ten Steps (HowTo schema) · Wheel Rules · RTP and Payout Basics · How to Read Past Results Sensibly · Demo, Observation and Mobile Play · Common Beginner Mistakes · A Simple Beginner Session Plan · How to Play Safely · FAQ
- **/demo-online/**: Introduction · Is There a Demo? · What Demo Means for a Live Game Show · Why Users Search for Demo · How to Find Demo or Watch Mode · What You Can Learn Without Betting · Demo vs Real Money · Why Demo Results Do Not Predict · Fake Demo APKs · Mobile Demo and Payment Decisions · Best Practice for First Real-Money Session · FAQ
- **/online-casinos/**: Introduction · How Online Casinos Work · What Makes a Good Casino · How to Compare Like an Editor · Verified Partner: <Partner> (#partner) · Check Evolution Availability · Payment Methods · KYC · Bonuses · Mobile and Demo · Licensing and Red Flags · How to Register · Responsible Gambling · FAQ
- **/faqs/**: grouped H2s: About the Game · Results, RTP and Prediction · Playing and Access · Payments and Casinos · Comparisons, Safety and Site (each H2 holds 5–8 accordions)
- **/about-us/**: Who We Are · Our Purpose · What We Cover · What We Do Not Do · Editorial Approach · How We Research · India-Focused Coverage · Review Standards · Affiliate Disclosure · Responsible Gambling Commitment · Position on Prediction Content · Why Trust Us · FAQ
- **/responsible-gambling/**: 22 short H2s from "Our Position on Gambling" to "Responsible Gambling Checklist", including KIRAN helpline, self-exclusion, warning signs, family impact, bonuses. Never add design blocks here (plain prose).
- **/hindi/**: Hinglish (Devanagari + English game terms), same H2 order as homepage, `lang="hi-IN"`, body class `l-hi` (loads Mukta font via theme.css).
