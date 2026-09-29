# Exchange Floor

A market opens, and every claim arrives as a number with a check behind it.

This is the set the first portfolio video used.
- **Best for:** fintech, data tools, dev infrastructure, anything with real metrics
- **Palette:** ink `#0a0a0a`, paper `#f0ede8`, one signal accent: lime `#c8ff00` or amber `#ffb000`; muted `#8a8a8a`
- **Type:** Archivo 800 for headlines, JetBrains Mono for every number
- **Texture:** a faint 120px grid, a scrolling ticker tape, and HUD corners (clock, scene counter)
- **Signature move:** a clock ticks to the open bell, then a full-frame accent flash and a hard cut
- **Transitions:** an accent-colour block wipes across the frame; no crossfades
- **Sound:** a sub pulse, soft hi-hat ticks and a sine bell in the key of the music
- **Watch out:** it needs real numbers. With nothing to count, it's just a dark slide.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: title, feature, stat and end card. Use them for composition and ornament.
- `DESIGN.md`: Stitch's full token set. Open it only when you need an exact colour role or type size.
- `ref/f1-f4.html`: Tailwind reference markup. Lift the ornament (SVG, borders, textures), not the page layout.

## Audit notes
- Stitch frames load: no text fonts (they fell back to system fonts). Use the **Type** line above; it is the intended pairing.
- 16:9 fit at 1920x1080: all four frames fit.
- Sanitised on import: 2x placeholder links must not point at a registrable domain; added the Space Grotesk + JetBrains Mono links the frame referenced but never loaded.
- Every word in the Stitch frames is placeholder copy: NEXUS, nexus.example, 99.999%, 840 ns, SOC 2, "certified", "granted". Replace all of it with the project's own facts.
