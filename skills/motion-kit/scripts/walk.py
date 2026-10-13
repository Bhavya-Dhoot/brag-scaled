"""Walk a web app for a demo video: find every page, then record a planned tour as real screenshots.

    python walk.py map https://example.com --out walk       # every same-origin page: what is on it, what can be clicked
    python walk.py record plan.json --out demo              # run the tour for real; writes shots/ and demo.js for ref/demo.html

`map` crawls from the start page (and sitemap.xml when there is one), and for each page writes
its title, headings, sections, clickable things with a selector for each, the colours and fonts
in use, and a thumbnail. Read walk/map.md and look at walk/map.jpg, then write the plan: every
page should appear in it, or be listed as skipped with a reason.

A plan is {"base": url, "width": 1920, "height": 1080, "scale": 2, "steps": [...]}. Each step has
one action and optional "say" (the caption, seven words or fewer), "chapter" (the name of the
screen being entered), "point" (a selector the cursor should point at while the caption is read)
and "zoom": false. Without "point" the camera leans toward the busiest part of the view:

    {"go": "/pricing", "chapter": "Pricing", "say": "Three plans, one page"}
    {"scroll": "#faq"}            a selector, a pixel offset, or "+1.5" screens down. Add "fade": true on a page
                                  that animates as it scrolls (the views are cross-faded, not panned); a scroll
                                  of more than three screens is shown as one quick jump
    {"click": "text=Start free"}  any Playwright selector
    {"type": ["#email", "ada@example.com"]}
    {"hover": "nav a:nth-of-type(2)"}     {"key": "Escape"}     {"wait": 0.8}

`record` performs each step in a real browser and saves what the page looked like after it,
where the target was before it, and how far the page scrolled, so the engine can move a cursor
to the real button and pan the real page.

It is a tour, not a test run: it refuses to type into a password field or to press a submit
button on a site that is not running on this machine, so nothing is sent on anyone's behalf.
Cookie banners are answered with the decline or necessary-only button when one is found.

Requires: pip install playwright pillow, playwright install chromium
"""
import argparse, json, pathlib, re, sys
from urllib.parse import urljoin, urlparse

LOCAL = re.compile(r"^(localhost|127\.0\.0\.1|\[::1\]|.*\.localhost|.*\.test)$")
SKIP_EXT = re.compile(r"\.(pdf|zip|png|jpe?g|gif|webp|svg|ico|xml|txt|json|mp4|mov|webm|mp3|wav|css|js|woff2?)$", re.I)
DECLINE = re.compile(r"^(reject( all)?|decline( all)?|deny|refuse|necessary only|only necessary|essential only|no,? thanks)$", re.I)

PAGE_FACTS = r"""() => {
  const vis = e => { const r = e.getBoundingClientRect(), s = getComputedStyle(e); return r.width > 8 && r.height > 8 && s.visibility !== 'hidden' && s.display !== 'none' && +s.opacity > .05; };
  const sel = e => { if (e.id) return '#' + CSS.escape(e.id); const p = [];
    for (let n = e; n && n.nodeType === 1 && n !== document.body && p.length < 5; n = n.parentElement) {
      let i = 1, s = n; while ((s = s.previousElementSibling)) if (s.tagName === n.tagName) i++;
      p.unshift(n.tagName.toLowerCase() + ':nth-of-type(' + i + ')');
      if (n.parentElement && n.parentElement.id) { p.unshift('#' + CSS.escape(n.parentElement.id)); break; } }
    return p.join(' > '); };
  const txt = e => (e.innerText || e.value || e.getAttribute('aria-label') || e.getAttribute('placeholder') || e.title || '').replace(/\s+/g, ' ').trim().slice(0, 48);
  const y = e => Math.round(e.getBoundingClientRect().top + scrollY);
  const css = (e, k) => e ? getComputedStyle(e)[k] : '';
  const btn = [...document.querySelectorAll('button, a[class*=btn], a[class*=button], [role=button]')].find(e => vis(e) && !/rgba\(0, 0, 0, 0\)|transparent/.test(css(e, 'backgroundColor')));
  return {
    title: document.title, desc: (document.querySelector('meta[name=description]') || {}).content || '',
    heads: [...document.querySelectorAll('h1, h2')].filter(vis).slice(0, 14).map(e => ({ tag: e.tagName.toLowerCase(), text: txt(e), y: y(e) })),
    sections: [...document.querySelectorAll('section[id], main [id], [id][class*=section]')].filter(vis).slice(0, 24).map(e => ({ sel: '#' + CSS.escape(e.id), y: y(e) })),
    links: [...document.querySelectorAll('a[href]')].map(a => a.href),
    actions: [...document.querySelectorAll('a[href], button, [role=button], input:not([type=hidden]), select, textarea, summary')].filter(vis).slice(0, 70)
      .map(e => ({ kind: e.tagName.toLowerCase() + (e.type && e.tagName === 'INPUT' ? ':' + e.type : ''), text: txt(e), sel: sel(e), y: y(e) })),
    height: document.documentElement.scrollHeight,
    look: { bg: css(document.body, 'backgroundColor'), ink: css(document.body, 'color'), accent: css(btn, 'backgroundColor'),
            body: css(document.body, 'fontFamily').split(',')[0], head: css(document.querySelector('h1, h2'), 'fontFamily').split(',')[0] } };
}"""

BARS = r"""() => { let top = 0, bottom = 0; const vw = innerWidth, vh = innerHeight;
  for (const e of document.querySelectorAll('body *')) { const s = getComputedStyle(e); if (s.position !== 'fixed' && s.position !== 'sticky') continue;
    const r = e.getBoundingClientRect(); if (r.width < vw * .6 || r.height < 8 || r.height > vh * .3 || s.visibility === 'hidden' || +s.opacity < .05) continue;
    if (r.top <= 4 && r.bottom > 0) top = Math.max(top, r.bottom); if (r.bottom >= vh - 4) bottom = Math.max(bottom, vh - r.top); }
  return { top: Math.round(top), bottom: Math.round(bottom) }; }"""


def settle(page, seconds=0.6):
    try:
        page.wait_for_load_state("networkidle", timeout=4000)
    except Exception:
        pass
    page.wait_for_timeout(int(seconds * 1000))


def decline_cookies(page):
    for b in page.locator("button, [role=button], a").all()[:80]:
        try:
            if DECLINE.match((b.inner_text(timeout=200) or "").strip()) and b.is_visible():
                b.click(timeout=800); page.wait_for_timeout(300); return True
        except Exception:
            continue
    return False


def norm(url):
    u = urlparse(url)
    return f"{u.scheme}://{u.netloc}{u.path.rstrip('/') or '/'}"


def detail_focus(path, w, h):
    """Where the detail is in a screenshot, and how far to lean in: [x, y, zoom]. A sparse view (a quote
    on an empty page) gets a tight frame around what is there, up to 1.9x; a full one gets the centre of
    its busiest 60%, at 1.2x. The player leans the camera there while a caption is read, so a held view
    still moves and small text becomes readable."""
    try:
        from PIL import Image, ImageFilter
    except ImportError:
        return None
    px = Image.open(path).convert("L").resize((96, 54)).filter(ImageFilter.FIND_EDGES).tobytes()
    pts = [(x, y) for y in range(6, 53) for x in range(1, 95) if px[y * 96 + x] > 48]      # skips a header strip and the border
    if len(pts) > 6:
        xs, ys = sorted(p[0] for p in pts), sorted(p[1] for p in pts); cut = len(pts) // 50  # ignore the stray 2% at each end
        x0, x1, y0, y1 = xs[cut], xs[-1 - cut], ys[cut], ys[-1 - cut]
        z = min(1.9, .8 / max((x1 - x0 + 4) / 96, (y1 - y0 + 4) / 54))
        if z > 1.25:
            return [round((x0 + x1) / 2 / 96 * w), round((y0 + y1) / 2 / 54 * h), round(z, 2)]
    best, at = -1, (48, 27)
    for cy in range(18, 37, 3):
        for cx in range(31, 66, 3):
            v = sum(px[y * 96 + x] for y in range(cy - 16, cy + 16, 2) for x in range(cx - 29, cx + 29, 2))
            if v > best:
                best, at = v, (cx, cy)
    return [round(at[0] / 96 * w), round(at[1] / 54 * h), 1.2]


def sheet(files, labels, out, cols=4, w=480):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return
    ims = [Image.open(f).convert("RGB") for f in files]
    h = int(w * ims[0].height / ims[0].width); rows = -(-len(ims) // cols)
    s = Image.new("RGB", (cols * w, rows * (h + 22)), "#222")
    for k, im in enumerate(ims):
        x, y = (k % cols) * w, (k // cols) * (h + 22)
        s.paste(im.resize((w, h)), (x, y + 22)); ImageDraw.Draw(s).text((x + 6, y + 5), labels[k][:70], fill="#fff")
    s.save(out, quality=84)


def cmd_map(a):
    from playwright.sync_api import sync_playwright
    out = pathlib.Path(a.out); (out / "thumbs").mkdir(parents=True, exist_ok=True)
    start = norm(a.url); origin = urlparse(start).netloc
    queue, seen, pages = [start], {start}, []
    with sync_playwright() as p:
        b = p.chromium.launch(); page = b.new_page(viewport={"width": a.width, "height": a.height})
        try:  # a sitemap names pages nothing links to
            r = page.request.get(urljoin(start, "/sitemap.xml"), timeout=8000)
            for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text() if r.ok else ""):
                u = norm(loc)
                if urlparse(u).netloc == origin and u not in seen and not SKIP_EXT.search(u):
                    seen.add(u); queue.append(u)
        except Exception:
            pass
        while queue and len(pages) < a.max:
            url = queue.pop(0)
            try:
                resp = page.goto(url, timeout=30000, wait_until="load"); settle(page, 0.8)
            except Exception as e:
                pages.append({"url": url, "error": str(e)[:120]}); continue
            if len(pages) == 0:
                decline_cookies(page)
            if norm(page.url) != url and norm(page.url) in {x["url"] for x in pages}:
                continue                                        # a redirect to a page already walked
            f = page.evaluate(PAGE_FACTS); f["url"] = url; f["status"] = resp.status if resp else None
            f["thumb"] = f"thumbs/{len(pages):02d}.jpg"; page.screenshot(path=str(out / f["thumb"]), type="jpeg", quality=70)
            for link in f.pop("links"):
                u = norm(link)
                if urlparse(u).netloc == origin and u not in seen and not SKIP_EXT.search(u):
                    seen.add(u); queue.append(u)
            pages.append(f)
        b.close()
    left = [u for u in queue]
    (out / "map.json").write_text(json.dumps({"start": start, "pages": pages, "not_walked": left}, indent=1), encoding="utf-8")
    md = [f"# {origin}: {len(pages)} pages walked" + (f", {len(left)} more found but not walked (raise --max)" if left else ""), ""]
    for f in pages:
        path = urlparse(f["url"]).path
        if "error" in f:
            md += [f"## {path}", f"could not open: {f['error']}", ""]; continue
        md += [f"## {path}", f"{f['title']} | {f['height'] / a.height:.1f} screens tall | {f['look']['head']} / {f['look']['body']} | bg {f['look']['bg']} ink {f['look']['ink']} accent {f['look']['accent']}",
               "headings: " + "; ".join(f"{h['text']} (y {h['y']})" for h in f["heads"] if h["text"]),
               "sections: " + ", ".join(f"{s['sel']} (y {s['y']})" for s in f["sections"]), "actions:"]
        md += [f"- {x['kind']} \"{x['text']}\" `{x['sel']}` (y {x['y']})" for x in f["actions"][:28] if x["text"]] + [""]
    (out / "map.md").write_text("\n".join(md), encoding="utf-8")
    ok = [f for f in pages if "error" not in f]
    if ok:
        sheet([out / f["thumb"] for f in ok], [urlparse(f["url"]).path for f in ok], out / "map.jpg")
    print(f"{len(pages)} pages -> {out / 'map.md'}, {out / 'map.json'}, {out / 'map.jpg'}" + (f"; {len(left)} not walked" if left else ""))


def cmd_record(a):
    from playwright.sync_api import sync_playwright
    plan = json.loads(pathlib.Path(a.plan).read_text(encoding="utf-8")); out = pathlib.Path(a.out); (out / "shots").mkdir(parents=True, exist_ok=True)
    w, h, scale = plan.get("width", 1920), plan.get("height", 1080), plan.get("scale", 2)
    local = bool(LOCAL.match(urlparse(plan["base"]).hostname or ""))
    steps, n = [], 0
    with sync_playwright() as p:
        b = p.chromium.launch(); page = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=scale).new_page()

        def shot():
            nonlocal n
            name = f"shots/s{n:03d}.jpg"; page.screenshot(path=str(out / name), type="jpeg", quality=a.quality); n += 1
            return name

        def box(sel):
            loc = page.locator(sel).first; loc.scroll_into_view_if_needed(timeout=6000); page.wait_for_timeout(250)
            r = loc.bounding_box()
            if not r:
                sys.exit(f"step {len(steps) + 1}: nothing visible matches {sel!r}")
            return loc, [round(r["x"]), round(r["y"]), round(r["width"]), round(r["height"])]

        for k, st in enumerate(plan["steps"]):
            kind = next((x for x in ("go", "scroll", "click", "type", "hover", "key", "wait") if x in st), None)
            if not kind:
                sys.exit(f"step {k + 1} has no action: {st}")
            rec = {"kind": kind, "say": st.get("say", ""), "chapter": st.get("chapter", ""), "zoom": st.get("zoom", True), "dur": st.get("dur")}
            y0 = page.evaluate("scrollY") if steps else 0
            if kind == "go":
                page.goto(urljoin(plan["base"], st["go"]), timeout=30000, wait_until="load"); settle(page, st.get("settle", 1.0))
                if not steps:
                    decline_cookies(page)
                rec["shots"] = [shot()]; rec["nav"] = True
            elif kind == "scroll":
                tgt, bars = st["scroll"], page.evaluate(BARS)
                top = page.evaluate("document.documentElement.scrollHeight - innerHeight")
                if isinstance(tgt, str) and tgt.startswith("+"):
                    y1 = y0 + float(tgt) * h
                elif isinstance(tgt, (int, float)):
                    y1 = tgt
                else:
                    y1 = page.evaluate("s => document.querySelector(s).getBoundingClientRect().top + scrollY", tgt) - bars["top"] - 24
                y1 = max(0, min(top, round(y1))); far = abs(y1 - y0) > 3 * h or bool(st.get("jump"))
                # near: stop every 0.8 screens so each pan joins two real views. far, or a page that animates on scroll: one look at the destination
                hops = 1 if far or st.get("fade") else max(1, -(-abs(y1 - y0) // int(h * .8)))
                rec["shots"], rec["ys"] = [], []
                for j in range(1, hops + 1):
                    y = round(y0 + (y1 - y0) * j / hops); page.evaluate("y => scrollTo({top: y, behavior: 'instant'})", y)
                    page.wait_for_timeout(int((st.get("settle", 0.7) if j == hops else 0.3) * 1000))
                    rec["ys"].append(page.evaluate("scrollY")); rec["shots"].append(shot())
                rec["bars"] = bars; rec["move"] = "fade" if st.get("fade") else "jump" if far else "pan"
            elif kind in ("click", "hover", "type"):
                sel = st[kind][0] if kind == "type" else st[kind]
                loc, rec["box"] = box(sel)
                rec["y_before"] = page.evaluate("scrollY")       # scroll_into_view may have moved the page
                rec["pre"] = shot() if rec["y_before"] != y0 else None
                url0 = page.url
                if kind == "hover":
                    loc.hover(); page.wait_for_timeout(350); rec["shots"] = [shot()]
                elif kind == "click":
                    if not local and not st.get("allow_submit") and loc.evaluate("e => (e.type === 'submit' || (e.tagName === 'BUTTON' && !e.type)) && !!e.closest('form')"):
                        sys.exit(f"step {k + 1}: {sel!r} submits a form on a live site. A tour stops at the filled form; add \"allow_submit\": true only for a search box or the like.")
                    loc.click(timeout=8000); settle(page, st.get("settle", 0.8)); rec["shots"] = [shot()]
                else:
                    if not local and loc.evaluate("e => e.type === 'password'"):
                        sys.exit(f"step {k + 1}: will not type into a password field on a live site. Use a test account on a local build, or leave the logged-in screens out and say so.")
                    text = st["type"][1]; loc.click(); rec["shots"] = []
                    for j in range(0, len(text), max(1, -(-len(text) // 8))):   # at most eight looks at the field filling
                        loc.press_sequentially(text[j:j + max(1, -(-len(text) // 8))]); rec["shots"].append(shot())
                    rec["text"] = text
                rec["nav"] = norm(page.url) != norm(url0)
            elif kind == "key":
                page.keyboard.press(st["key"]); settle(page, st.get("settle", 0.6)); rec["shots"] = [shot()]
            else:
                page.wait_for_timeout(int(st["wait"] * 1000)); rec["shots"] = [shot()]
            if st.get("point"):
                r = page.locator(st["point"]).first.bounding_box()
                if r and 0 <= r["y"] < h and r["y"] + min(r["height"], h) > 0:
                    rec["point"] = [round(r["x"]), round(max(0, r["y"])), round(r["width"]), round(min(r["height"], h - max(0, r["y"])))]
                else:
                    print(f"   note: {st['point']!r} is not in view after step {k + 1}; the camera will choose for itself")
            if "point" not in rec:
                rec["focus"] = detail_focus(out / rec["shots"][-1], w, h)
            rec["y"] = page.evaluate("scrollY"); rec["url"] = urlparse(page.url).path + (("#" + urlparse(page.url).fragment) if urlparse(page.url).fragment else "")
            steps.append(rec); print(f"{k + 1:2d} {kind:6s} {str(st[kind])[:44]:44s} -> {rec['url']}  y={rec['y']}  {len(rec['shots'])} shot(s)")
        b.close()
    demo = {"base": plan["base"], "w": w, "h": h, "scale": scale, "steps": steps}
    (out / "demo.js").write_text("window.DEMO = " + json.dumps(demo) + ";", encoding="utf-8")
    files = [out / s for r in steps for s in r["shots"]]
    sheet(files, [f"{i + 1} {r['kind']} {r['say']}" for i, r in enumerate(steps) for _ in r["shots"]], out / "shots.jpg")
    print(f"{len(steps)} steps, {n} shots -> {out / 'demo.js'}, {out / 'shots.jpg'}")


def main():
    ap = argparse.ArgumentParser(description="Map a web app, or record a planned tour of it, for a demo video.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    m = sub.add_parser("map"); m.add_argument("url"); m.add_argument("--out", default="walk"); m.add_argument("--max", type=int, default=40)
    m.add_argument("--width", type=int, default=1920); m.add_argument("--height", type=int, default=1080)
    r = sub.add_parser("record"); r.add_argument("plan"); r.add_argument("--out", default="demo"); r.add_argument("--quality", type=int, default=88)
    a = ap.parse_args()
    (cmd_map if a.cmd == "map" else cmd_record)(a)


if __name__ == "__main__":
    main()
