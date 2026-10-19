---
name: evolution-game-emd-site
description: Build a complete, SEO-optimised, India-facing exact-match-domain (EMD) affiliate site for a live casino game show (Evolution Gaming or Galaxsys titles such as Ice Fishing, Tower Rush, Crazy Time, Funky Time, Dream Catcher, Monopoly Live, Lightning Storm, Aviator-style crash games) in the exact style of icefishing-game.co. Use this skill whenever the user asks for a site "like icefishing-game.co", a "game guide site", "live results / result tracker site", a casino game show landing site for India, an EMD site for a game keyword, or wants the Ahrefs research → homepage outline → extended page architecture → static HTML build workflow for any casino game. Also trigger when the user names a game domain (e.g. towerrushgame.co, icefishing-game.vip) and wants pages, a homepage outline, Hindi/regional versions, or a redirect "Play Now" page. Covers research, content rules, compliance, dark Arctic-style theme CSS, schema stack and static deployment.
---

# Evolution / Galaxsys Game Show EMD Site (icefishing-game.co pattern)

This skill reproduces the exact workflow and design used to build **icefishing-game.co**: an India-facing, informational-affiliate, static HTML site for one live casino game show, targeting the game's head keyword plus its "result / live score / tracker" cluster, with a `/play/` redirect to the affiliate partner.

The output is a folder of static HTML pages (one `index.html` per folder) + `sitemap.xml` + `robots.txt`, deployable to Cloudflare Pages / any static host.

## Workflow (do in this order)

### Step 1: Research (Ahrefs, country = IN)
Read `references/seo-research-workflow.md`. Pull:
1. `keywords-explorer-matching-terms` on the game name (`match_mode: terms`, `country: in`, `order_by: volume:desc`, `limit: 150`, select `keyword,volume,difficulty,cpc,parent_topic,intents`)
2. `keywords-explorer-related-terms` with `terms: also_rank_for` and `view_for: top_10`
3. `serp-overview` for the head term and the "result" term separately
4. `web_fetch` the reference site the user gives (if it fails, web_search the domain string and analyse the ranking competitor cluster instead)

Group keywords into intent clusters (head / results / how-to / demo / real-money / app-download / real-or-fake / prediction / where-to-play / provider). One intent = one page. State honestly which clusters are too thin for India and must be sections, not pages.

### Step 2: Homepage content outline
Read `references/homepage-outline.md`. Deliver the outline in the fixed format: SERP intelligence → voice/tone → primary + secondary keyword map with volumes → section-by-section H1/H2/H3 structure with per-section keywords → semantic/LSI entity terms → images + alt text → schema stack → meta title/description. Place the **Live Results & Stats** section high (right after Key Facts) because the results cluster usually out-volumes the head term.

### Step 3: Extended site architecture
Read `references/site-architecture.md`. Produce the tiered page map (results silo first), internal-linking silo map, utility/trust pages, and build order by ROI. Mark LOCKED-DATA pages (RTP, segment counts, max win) so every page uses identical figures.

### Step 4: Build the static site
Read `references/build-spec.md` and use the files in `assets/`:
- `assets/theme.css`: the exact dark Arctic theme (CSS vars, header, age gate, spec grid, callouts, do/don't cards, FAQ accordion, author box, sticky CTA, footer). Inline it in every page's `<style>`.
- `assets/reference-homepage.html`: the real icefishing-game.co homepage (partner name replaced by `{{PARTNER}}`). Copy its exact DOM structure and class names; swap game facts and copy.
- `assets/redirect-page.html`: the `/play/` and `/login/` noindex meta-refresh redirect to the affiliate link.
- `assets/schema-graph.json`: the `@graph` JSON-LD stack (Organization, WebSite, WebPage, BreadcrumbList, Article, VideoGame, FAQPage; HowTo on how-to pages).

Run `python3 scripts/scaffold_site.py <output-dir> --domain <domain> --game "<Game>" --affiliate "<url>"` to create the folder tree, redirect pages, robots.txt and a sitemap.xml you then update.

### Step 5: QA checklist (before delivering)
- Age gate present and `localStorage` key unique per site (`if_age` → change prefix)
- Every CTA to `/play/` has `rel="nofollow sponsored noopener noreferrer" target="_blank"`
- `/play/` and `/login/` are `noindex,nofollow` and excluded from sitemap
- All numeric facts match the LOCKED-DATA table across every page
- Canonical + hreflang (en-IN, hi-IN, x-default) on every page; Hindi page at `/hindi/` mirrors the homepage H2 order
- No "provably fair / server seed" wording on an Evolution wheel game (crash-game terminology only)
- No guaranteed-win, prediction-tool, hack or signal language anywhere; prediction section is a debunk
- Responsible gambling callout + KIRAN helpline 1800-599-0019 on every page; 30% tax (Sec 115BBJ / 194BA) mentioned on real-money content
- No author real names, company names or emails (anonymous "Editorial Team")
- Meta description ≤ 158 chars, keyword first, includes year, no "learn / discover / explained"
- No em dashes in copy

## Content rules (summary; full version in `references/content-rules.md`)
- Voice: informational-authoritative, second person, short sentences (12–18 words), class 8–9 reading level, rupees everywhere, "in India" 4–6 times naturally. Not hypey.
- Open each page with a plain, slightly casual intro (~8% of the page), then professional tone.
- Paragraph-first: tables/bullets/callouts capped at 30% of the page.
- Honesty is the ranking edge: history ≠ prediction, demo may not exist for live shows, no APK needed, Leaf RTP vs bonus RTP separated.
- Every section ends naturally; CTA rows after Results, Bonus Rounds, Real Money, Comparison and the FAQ.

## Default page set (icefishing-game.co)
`/` · `/how-to-play/` · `/demo-online/` · `/online-casinos/` · `/faqs/` · `/about-us/` · `/contact-us/` · `/responsible-gambling/` · `/terms-and-conditions/` · `/privacy-policy/` · `/cookie-policy/` · `/hindi/` (+ Hindi mirrors of each) · `/play/` + `/login/` (redirects, noindex). Add results/tracker, real-money, download, real-or-fake, state pages etc. per Step 3 when the user wants the larger 30–60 page build.

## Game fact sheet (Ice Fishing, Evolution): reuse pattern for other games
Provider Evolution Gaming · release 6 Aug 2025 · 53-segment wheel · Leaf 1 (23/53), Leaf 2 (23/53), Lil' Blues (4/53, up to 100x base / 1,000x), Big Oranges (2/53, up to 200x / 2,000x), Huge Reds (1/53, up to 500x / 5,000x) · RTP Leaf 97.10%, Lil' Blues 95.69%, Big Oranges 95.60%, Huge Reds 95.17% · min bet ~₹10 · round 20–45 s · no download · stablemates Crazy Time, Funky Time, Dream Catcher, Monopoly Live, Lightning Storm. For a new game, build the equivalent LOCKED-DATA sheet from the provider's official page before writing anything.
