# SEO research workflow (Ahrefs, India)

All pulls use `country: in` (or `IN`). These parameter sets are the ones that worked on the ice fishing / tower rush builds; others threw errors.

## 1. Keyword universe
`Ahrefs:keywords-explorer-matching-terms`
- `keywords`: game name (e.g. `ice fishing`): use the shortest seed, not "ice fishing game", so result/tracker/demo variants are included
- `match_mode: terms`, `order_by: volume:desc`, `limit: 150`
- `select: keyword,volume,difficulty,cpc,parent_topic,intents,traffic_potential`
- Optional `where`: `volume gte 50` + `keyword substring "<game>"`
- Field name is `difficulty`, NOT `keyword_difficulty` (errors)
- `terms: all` is reliable; `terms: also_talk_about` returns co-occurrence noise from unrelated geos, avoid it
- `terms: questions` returns thin results in this niche (demand is in result/score phrasing, not "what is / how to")

## 2. Co-ranking terms
`Ahrefs:keywords-explorer-related-terms`
- `keywords`: `<game> game, <game> casino` (two seeds together is fine)
- `terms: also_rank_for` (or `terms: all`), `view_for: top_10` (`view_for: terms` is invalid)
- `order_by: volume:desc`, `limit: 40–60`

## 3. Brand/navigational variants
`Ahrefs:keywords-explorer-search-suggestions` on the broad seed and on `<game> evolution`.

## 4. SERP composition
`Ahrefs:serp-overview`
- `keyword`, `country: IN`, `top_positions: 10–15`
- `select: position,title,url,type,domain_rating,url_rating,backlinks,refdomains,traffic,keywords,top_keyword,top_keyword_volume,page_type`
- Run separately for the head term and for `<game> result`: the two SERPs differ (head term may be dominated by DR 60–99 platform/operator pages; the result cluster is usually won by DR 0–44 EMD/affiliate sites).

## 5. Reference site
`web_fetch` the user's reference domain. These sites are often not indexed or block fetch; if so, `web_search` the domain string and the top ranking EMD competitors (e.g. for ice fishing: ice-fishing.in, icefishing.show, playicefishing.com, icefishing-live.com, icefishing.casino) and derive structure from them. Say so explicitly instead of inventing fetched content.

Check the Ahrefs `doc` tool for a tool's parameters before the first call if unsure.

## Intent clusters to bucket into (one page per bucket when India volume justifies it)
| Cluster | Typical keywords | Usual verdict |
|---|---|---|
| Head | `<game> game`, `<game> online`, `<game> casino` | Homepage |
| Results | `result`, `result today`, `live score`, `tracker`, `casino scores`, `big win` | Biggest cluster, dedicated `/results` page (+ tracker, big-win spokes if volume) |
| How to play | `how to play`, `rules`, `history`, `original` | `/how-to-play/` with HowTo schema |
| Demo | `demo`, `free play`, `demo apk` | `/demo-online/` (honest: live shows rarely have true demo) |
| Real money | `real money`, `gambling game`, `betting game` | `/real-money/` or section on homepage |
| Where to play | `casino`, `where to play`, operator names | `/online-casinos/` (money page) |
| App/download | `app`, `apk`, `download` | page only if cluster ≥ ~500/mo; honest "no APK needed" |
| Real or fake | `real or fake`, `is it real` | `/is-<game>-real/` trust page |
| Prediction | `prediction`, `predictor`, `hack` | debunk section/page, never a tool |
| Provider | `<game> evolution`, `evolution gaming` | authority page; "vs Crazy Time" comparison terms have negligible India volume, keep as a section |
| Legal | `legal in india`, `<game> india` | YMYL structural page |

Report the content-style split of competitors (paragraph vs points) and a recommended word count from competitor word counts, then cap points/tables at 30%.

## Compliance filter
Exclude from targets: operator login pages as ranking targets, prediction/signal tools, bonus-stacking promo pages, under-18 anything. India's Promotion and Regulation of Online Gaming Act 2025 context must be acknowledged on the legal page; the site stays informational.
