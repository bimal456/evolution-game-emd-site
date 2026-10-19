#!/usr/bin/env python3
"""Scaffold the folder tree for an Evolution/Galaxsys game show EMD site.

Usage:
  python3 scaffold_site.py OUT_DIR --domain icefishing-game.co --game "Ice Fishing" \
      --affiliate "https://partner.example/click?pid=1&sub1={your_click_id}" \
      [--pages how-to-play,demo-online,online-casinos,faqs,about-us,contact-us,responsible-gambling,terms-and-conditions,privacy-policy,cookie-policy] \
      [--hindi] [--extra results,real-money,download]

Creates: OUT_DIR/<page>/index.html placeholders (with the shared shell marker),
OUT_DIR/play/index.html + OUT_DIR/login/index.html redirects, robots.txt, sitemap.xml,
assets/ (theme.css copied for reference; pages should inline it).
The page files are placeholders: Claude writes the real HTML into them using
assets/reference-homepage.html as the structural model.
"""
import argparse, datetime, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
DEFAULT_PAGES = ["how-to-play", "demo-online", "online-casinos", "faqs", "about-us",
                 "contact-us", "responsible-gambling", "terms-and-conditions",
                 "privacy-policy", "cookie-policy"]


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--domain", required=True)
    ap.add_argument("--game", required=True)
    ap.add_argument("--affiliate", required=True)
    ap.add_argument("--pages", default=",".join(DEFAULT_PAGES))
    ap.add_argument("--extra", default="")
    ap.add_argument("--hindi", action="store_true")
    a = ap.parse_args()

    pages = [p for p in a.pages.split(",") if p]
    pages += [p for p in a.extra.split(",") if p]
    base = f"https://{a.domain}"
    today = datetime.date.today().isoformat()

    # redirect pages
    with open(os.path.join(ASSETS, "redirect-page.html"), encoding="utf-8") as f:
        redirect = f.read().replace("{{AFFILIATE_URL}}", a.affiliate).replace("Ice Fishing", a.game)
    for r in ("play", "login"):
        write(os.path.join(a.out, r, "index.html"), redirect)

    # placeholders
    urls = [f"{base}/"]
    write(os.path.join(a.out, "index.html"), f"<!-- HOMEPAGE: build from assets/reference-homepage.html for {a.game} -->\n")
    for p in pages:
        write(os.path.join(a.out, p, "index.html"), f"<!-- PAGE /{p}/ for {a.game}: see references/homepage-outline.md -->\n")
        urls.append(f"{base}/{p}/")
    if a.hindi:
        write(os.path.join(a.out, "hindi", "index.html"), "<!-- HINDI homepage mirror, lang=hi-IN, body.l-hi -->\n")
        urls.append(f"{base}/hindi/")
        for p in pages:
            if p in ("terms-and-conditions", "privacy-policy", "cookie-policy", "about-us", "contact-us", "responsible-gambling", "faqs", "how-to-play", "demo-online", "online-casinos"):
                write(os.path.join(a.out, "hindi", p, "index.html"), f"<!-- HINDI mirror of /{p}/ -->\n")
                urls.append(f"{base}/hindi/{p}/")

    # assets
    os.makedirs(os.path.join(a.out, "assets"), exist_ok=True)
    shutil.copy(os.path.join(ASSETS, "theme.css"), os.path.join(a.out, "assets", "theme.css"))

    # robots + sitemap
    write(os.path.join(a.out, "robots.txt"),
          f"User-agent: *\nAllow: /\nDisallow: /play/\nDisallow: /login/\n\nSitemap: {base}/sitemap.xml\n")
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        pr = "1.0" if u.endswith(f"{a.domain}/") else "0.8"
        sm.append(f"  <url><loc>{u}</loc><lastmod>{today}</lastmod><changefreq>weekly</changefreq><priority>{pr}</priority></url>")
    sm.append("</urlset>")
    write(os.path.join(a.out, "sitemap.xml"), "\n".join(sm) + "\n")

    print(f"Scaffolded {len(urls)} indexable URLs + 2 redirects in {a.out}")
    for u in urls:
        print(" ", u)


if __name__ == "__main__":
    sys.exit(main())
