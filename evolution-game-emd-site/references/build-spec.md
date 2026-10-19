# Build spec: HTML shell, theme, components, schema

Everything below is taken from the live icefishing-game.co pages. Open `assets/reference-homepage.html` for the exact markup and `assets/theme.css` for the exact CSS. Pages are single self-contained HTML files (CSS inlined in `<style>`, SVG illustrations inline, Google Fonts linked), one folder per URL with `index.html`.

## `<head>` (every page)
```
<!doctype html><html lang="en-IN">
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>…</title><meta name="description" content="…">
<link rel="canonical" href="https://DOMAIN/path/">
<link rel="alternate" hreflang="en-IN" href="https://DOMAIN/path/">
<link rel="alternate" hreflang="hi-IN" href="https://DOMAIN/hindi/path/">
<link rel="alternate" hreflang="x-default" href="https://DOMAIN/path/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#08161f">
og:type website · og:locale en_IN · og:site_name · og:title · og:description · og:url · og:image /assets/og.png · twitter:card summary_large_image
<link rel="icon" href="data:image/svg+xml;utf8,…"> (inline SVG favicon, brand mark)
preconnect fonts.googleapis.com + fonts.gstatic.com
<link href="https://fonts.googleapis.com/css2?family=Schibsted+Grotesk:wght@600;700;800&family=Hanken+Grotesk:wght@400;500;600;700&family=Fragment+Mono:wght@400&family=Mukta:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style> …theme.css… </style>
<script type="application/ld+json"> …@graph… </script>
```

## Theme tokens (theme.css `:root`)
`--bg:#08161f --bg2:#0c1e2a --card:#102634 --card2:#163140 --line:rgba(120,175,205,.16) --blue:#2bb8e6 --blue2:#a6e4f7 --pink:#ff8a3d --pink2:#ffc08a --mint:#4ade80 --amber:#fbbf24 --coral:#f43f5e --violet:#a78bfa --text:#eaf4f9 --muted:#a9c2ce --radius:16px --maxw:1080px`
Body: Hanken Grotesk 17px/1.7 on a dark navy with two radial glows (blue top-right, orange top-left). Headings: Schibsted Grotesk. Hindi pages: body class `l-hi` switches to Mukta.
For a different game, swap `--blue`/`--pink` accents (e.g. Tower Rush: violet + amber) and the logo mark; keep everything else.

## Body order
1. `div.agegate#agegate` > `.ag-card` (h2 "Are you 18 or older?", paragraph, `.ag-btns`: `button.btn.btn-cta onclick="trgOk()"` "I am 18+" + `a.btn.btn-ghost href="https://www.google.com"` "Exit", `.ag-rg` line with KIRAN helpline). JS at end of body: `trgOk()` sets `localStorage` key and adds `.hide`; on load, if key set hide gate else `body.locked`.
2. `a.skip` → `#main`
3. `header.hd` > `.wrap.hd-in`: `a.brand` (inline SVG `logo-mark` + `.logo-txt` "Ice<b>Fishing</b>") · `span.hd-spacer` · `a.btn.btn-cta.hd-cta` Play Now (/play/) · `a.btn.btn-cta.hd-login` Login (/login/) · `button.burger` (3 spans) toggling `nav.mnav`
4. `div.subnav-wrap` > `nav.subnav.wrap` with every page link, current page gets class `on`
5. `nav.mnav` mobile duplicate of subnav + Play Now button
6. `main#main` > `div.wrap`: `nav.crumbs` (Home / Page) · `div.phead` (span.eyebrow, h1, p.lead, div.cta-row) · `div.rstrip` (4 `.rs` chips: `<i>label</i><b>value</b>`) · `figure.fig.hero` SVG · prose · `div.spec-grid` of `div.spec` (`<span>label</span><b>value</b>`) · H2 sections
7. `aside.author` (`.au-av` logo, `.au-bd` strong + span + span.au-meth)
8. `div.sticky-cta` > `.sc-in` (`.sc-tx` b + small, `a.btn.btn-cta`)
9. `footer.ft#responsible` > `.wrap` > `.ft-top` (`.fbrand` logo + 2 p incl `p.rg-line`; three `.fcol` h4+ul) + `.ft-bot` (affiliate disclaimer p, `p.disc` 18+/tax/copyright)

## Components (class → use)
- `.tw` table wrapper (horizontal scroll); tables plain `<table>` with `thead`
- `.call.call-info` / `.call-rg` / `.call-warn` / `.call-scam` / `.call-tip` → `.call-ic` (single glyph ℹ ❤ ⚠ ✕ ✓) + `.call-bd` (strong title + text)
- `.do2` > `.do.do-ok` / `.do.do-no` → h4 + ul (prediction section)
- `ol.steps > li` with `<span>` step number then text (how-to)
- `.cards > .card` (icon svg + h3 + p) for criteria/features
- `.faq > details > summary` + `div.faq-a` (native accordion, caret via CSS `:after`)
- `.cta-row > .btn` (CTA after key sections)
- `figure.fig` wrapping inline SVG illustrations with `<figcaption>`; every SVG gets `role="img"` + `<title>` with keyword alt text
- `.eyebrow` small uppercase label; `.lead` larger intro paragraph; `.prose` wrapper for long text

## Illustrations (inline SVG, keyword-named `<title>`)
Homepage uses 7: hero live wheel with sample results · 53-segment wheel layout with counts · how-to step flow · three bonus rounds · RTP bars · India payments (UPI/Paytm/PhonePe/Bank/Crypto) · (optional) mobile/app. Inner pages 2–4 each. Keep SVGs simple (rects, circles, text) in the theme palette.

## Links and CTAs
All affiliate CTAs: `href="/play/" target="_blank" rel="nofollow sponsored noopener noreferrer" data-cta="play"`. `/play/` and `/login/` are `assets/redirect-page.html` with `{{AFFILIATE_URL}}` (keep `{your_click_id}` sub-ID macro and `sub2=<site tag>` if the network uses it). Internal links are root-relative.

## JSON-LD `@graph` (assets/schema-graph.json)
Organization(#org) · WebSite(#website) · WebPage(#webpage, breadcrumb → #breadcrumb) · BreadcrumbList · Article (headline = H1, author Organization "Editorial Team", datePublished/dateModified) · VideoGame (name, gamePlatform Web/Android/iOS, genre "Live casino game show", author Organization provider) · FAQPage (mainEntity = the on-page FAQ, same wording). How-to pages add HowTo + HowToStep. No AggregateRating/Review unless a real rating is displayed. Update the VideoGame description per game (the reference file carried a copy-paste error from Tower Rush; always re-write it).

## Sitemap / robots
`sitemap.xml` lists every indexable page (EN + Hindi) with `lastmod`; exclude /play/ and /login/. `robots.txt`: allow all, `Disallow: /play/`, `Disallow: /login/`, `Sitemap:` line. Optional `site.webmanifest`, `/sitemap/index.html` HTML sitemap, `/assets/og.png`, `/assets/logo.png`, favicons.

## Deployment
Cloudflare Pages (preferred over Vercel for iGaming): private GitHub repo → Pages project → custom domain already on Cloudflare DNS. `.htaccess` is ignored there; HTTPS redirect is automatic. If browser upload stalls, use `wrangler pages deploy <dir> --project-name <name>` with an API token the user creates.
