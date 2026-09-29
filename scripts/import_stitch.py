"""Import a Google Stitch export into skills/brag-styles/sets/.

For each set it copies the DESIGN.md, compresses the four reference screenshots to WebP,
and keeps each frame's HTML as a reference implementation. Remote images are downloaded
beside it and the HTML is sanitised:
  * invented regalia only: no real patent office, no transit-authority roundel
  * no unverified CJK or Arabic script used as ornament
  * placeholder links point at nexus.example, never a registrable real domain
  * broken or missing font links are fixed

Usage: python scripts/import_stitch.py <stitch-export-dir>
Re-running overwrites the sets it maps and leaves everything else alone.
"""
import hashlib, json, pathlib, re, shutil, sys, urllib.request
from PIL import Image

ROOT = pathlib.Path(__file__).resolve().parents[1] / "skills" / "brag-styles" / "sets"

# set slug -> (DESIGN.md folder, frame-folder keywords, extra asset folders)
SETS = {
    "exchange-floor": ("quant_brutalism", ["market_open_title", "microsecond_routing_feature", "deterministic_proofs_stat", "market_does_not_wait"], []),
    "riso-zine": ("riso_underground", ["riso_zine"], []),
    "patent-office": ("patent_blueprint_drafting_system", ["patent_blueprint"], []),
    "stop-motion-collage": ("stop_motion_paper_collage", ["stop_motion_collage"], []),
    "extra-extra": ("broadsheet_editorial", ["broadsheet"], []),
    "insert-coin": ("8_bit_arcade_crt_terminal", ["8_bit_arcade"], []),
    "the-receipt": ("thermal_till", ["thermal_receipt"], []),
    "transit-map": ("metro_signage_transit_wayfinding", ["transit_map"], []),
    "title-sequence": ("kinetic_cut", ["saul_bass"], []),
    "museum-placard": ("gallery_deadpan", ["gallery_deadpan"], []),
    "shahi-darbar": ("shahi_darbar", ["mughal_miniature"], []),
    "jaipur-block-print": ("pink_city_rajputana_storyboard", ["jaipur_pink_city"], []),
    "court-of-versailles": ("versailles_baroque", ["court_of_versailles"], []),
    "illuminated-manuscript": ("tudor_scriptorium", ["tudor_manuscript"], []),
    "forbidden-city": ("forbidden_city_imperial_handscroll", ["forbidden_city"], ["imperial_cinnabar_seal_chop_nx"]),
    "sultans-firman": ("imperial_firman_storyboard", ["ottoman_firman"], ["nexus_ottoman_imperial_latin_monogram"]),
    "byzantine-gold": ("imperial_revetment", ["byzantine_gold"], []),
    "maharaja-deco": ("maharaja_deco_bombay_1935", ["maharaja_deco"], ["maharaja_deco_monogram_crest"]),
}

TEXT_FIXES = [  # (pattern, replacement, reason)
    (r"U\.S\. PATENT OFFICE", "OFFICE OF INVENTIONS", "no real government office"),
    (r"UNITED STATES PATENT SPECIFICATION", "PATENT SPECIFICATION", "no real government office"),
    (r"USPTO", "OFFICE OF INVENTIONS", "no real government office"),
    (r"nexus\.markets", "nexus.example", "placeholder links must not point at a registrable domain"),
    ("[一-鿿]+", "", "no unverified Chinese characters"),
    ("[؀-ۿ]+", "", "no Arabic script as ornament"),
    # the transit roundel (red ring + blue bar) is a registered trademark; make it a diamond
    (r'<div class="w-32 h-32 rounded-full bg-primary-container flex items-center justify-center">\s*<div class="w-20 h-20 rounded-full bg-surface-container-lowest"></div>',
     '<div class="w-28 h-28 rotate-45 bg-primary-container flex items-center justify-center">\n<div class="w-16 h-16 bg-surface-container-lowest"></div>', "no transit-authority roundel"),
    # Stitch wrote an invalid axis range for Bricolage Grotesque, so the font never loaded
    (r"family=Bricolage\+Grotesque:opsz,wght@12\.\.96,700;800", "family=Bricolage+Grotesque:opsz,wght@12..96,700..800", "font link returned 400"),
]
QUANT_FONTS = ('<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700'
               '&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet"/>')


def localise_images(html, asset_dir, rel):
    urls = sorted(set(re.findall(r"https://lh\d\.googleusercontent\.com/[^\"')\s>,]+", html)))  # commas end srcset/CSS lists
    for url in urls:
        with urllib.request.urlopen(url, timeout=60) as r:
            data, ctype = r.read(), r.headers.get("Content-Type", "image/png")
        ext = {"image/jpeg": ".jpg", "image/webp": ".webp", "image/png": ".png"}.get(ctype.split(";")[0], ".png")
        name = hashlib.sha1(url.encode()).hexdigest()[:12] + ext
        asset_dir.mkdir(parents=True, exist_ok=True)
        (asset_dir / name).write_bytes(data)
        html = html.replace(url, f"{rel}/{name}")
    return html, len(urls)


def sanitise(html, slug, log):
    for pat, rep, why in TEXT_FIXES:
        html, n = re.subn(pat, rep, html)
        if n:
            log.append(f"{n}x {why}")
    if slug == "exchange-floor" and "fonts.googleapis.com/css2?family=Space" not in html:
        html = html.replace("</head>", QUANT_FONTS + "\n</head>", 1)
        log.append("added the Space Grotesk + JetBrains Mono links the frame referenced but never loaded")
    return html


def webp(src, dst):
    im = Image.open(src).convert("RGB")
    im.thumbnail((1600, 1600))
    im.save(dst, "WEBP", quality=82, method=6)


def rerender(out):
    """Screenshot the sanitised HTML, so the reference images match the fixed markup
    (Stitch's own screenshots still show the text that was removed)."""
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--enable-gpu", "--use-angle=d3d11", "--ignore-gpu-blocklist", "--force-color-profile=srgb"])
        for html in sorted(out.glob("*/ref/*.html")):
            pg = b.new_page(viewport={"width": 1600, "height": 1280})
            pg.goto(html.as_uri(), wait_until="networkidle", timeout=90000)
            pg.evaluate("document.fonts.ready")
            png = html.parent.parent / "frames" / (html.stem + ".png")
            pg.screenshot(path=str(png), full_page=True)
            webp(png, png.with_suffix(".webp"))
            png.unlink()
            pg.close()
        b.close()


def main(src):
    src = pathlib.Path(src)
    dirs = [d for d in src.iterdir() if d.is_dir()]
    report = {}
    for slug, (design, keys, extras) in SETS.items():
        out = ROOT / slug
        for sub in ("frames", "ref", "assets"):
            shutil.rmtree(out / sub, ignore_errors=True)
        (out / "frames").mkdir(parents=True, exist_ok=True)
        (out / "ref").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src / design / "DESIGN.md", out / "DESIGN.md")
        frames = sorted([d for d in dirs if d.name.startswith("frame_") and any(k in d.name for k in keys)],
                        key=lambda d: int(re.match(r"frame_0?(\d)", d.name).group(1)))
        assert len(frames) == 4, (slug, [d.name for d in frames])
        log, imgs = [], 0
        for i, d in enumerate(frames, 1):
            webp(d / "screen.png", out / "frames" / f"f{i}.webp")
            html = (d / "code.html").read_text(encoding="utf-8")
            html, n = localise_images(html, out / "assets", "../assets")
            imgs += n
            (out / "ref" / f"f{i}.html").write_text(sanitise(html, slug, log), encoding="utf-8")
        for e in extras:
            webp(src / e / "screen.png", out / "frames" / f"{e}.webp")
            html, n = localise_images((src / e / "code.html").read_text(encoding="utf-8"), out / "assets", "../assets")
            imgs += n
            (out / "ref" / f"{e}.html").write_text(sanitise(html, slug, log), encoding="utf-8")
        report[slug] = {"frames": [d.name for d in frames], "extras": extras, "images_localised": imgs, "fixes": sorted(set(log))}
        print(f"{slug:24s} frames=4 extras={len(extras)} images={imgs} fixes={len(set(log))}")
    rerender(ROOT)
    (ROOT / "import-report.json").write_text(json.dumps(report, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1])
