# Stop-Motion Collage

Torn paper, tape and cutouts animated at 12 fps, with a slightly handmade wobble.

- **Best for:** consumer apps, food, lifestyle, education, kids' products
- **Palette:** kraft `#c9a27a`, cream `#f7efe2`, tomato `#e4572e`, teal `#17a398`, ink `#1d1d1d`
- **Type:** Bricolage Grotesque for headlines; cut-out ransom letters for single words only
- **Texture:** torn paper edges, masking tape, soft 2-layer paper shadows, cardboard grain
- **Signature move:** everything moves on 12 fps "twos" with a slight per-frame position jitter, so it reads as real stop-motion
- **Transitions:** a hand-slid card swap, or a paper sheet pulled off the top like a notepad
- **Sound:** paper rustle, a tape rip, a pencil tap, and a ukulele or plucked-marimba bed
- **Watch out:** too much jitter reads as a bug. Keep it to about 2px.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: title, feature, stat and end card. Use them for composition and ornament.
- `DESIGN.md`: Stitch's full token set. Open it only when you need an exact colour role or type size.
- `ref/f1-f4.html`: Tailwind reference markup. Lift the ornament (SVG, borders, textures), not the page layout.

## Audit notes
- Stitch frames load: no text fonts (they fell back to system fonts). Use the **Type** line above; it is the intended pairing.
- 16:9 fit at 1920x1080: all four frames fit.
- Sanitised on import: 1x font link returned 400; 2x placeholder links must not point at a registrable domain.
- `assets/` holds 1 Stitch-generated image(s): mood reference only, never in the video.
- Every word in the Stitch frames is placeholder copy: NEXUS, nexus.example, 99.999%, 840 ns, SOC 2, "certified", "granted". Replace all of it with the project's own facts.
