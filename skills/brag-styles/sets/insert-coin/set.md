# Insert Coin

The product as an arcade cabinet game: a score counter, levels and a high-score table.

- **Best for:** games, playful consumer apps, dev tools with a sense of humour
- **Palette:** CRT black `#0b0b12`, neon cyan `#34f5ff`, magenta `#ff3fa4`, pixel yellow `#ffe14d`
- **Type:** Press Start 2P for display, VT323 for readouts, Silkscreen for labels
- **Texture:** scanlines, slight RGB fringing, a bezel vignette, a dithered 2-colour sky
- **Signature move:** a "LEVEL UP" beat per feature, with the score counter rolling up to the real stat; the end card is the high-score table with the URL as the #1 initials
- **Transitions:** a pixel-block dissolve, or a CRT power-off to a line and back on
- **Sound:** a chiptune bed (square and triangle waves, in key), coin insert, level-up arpeggio
- **Watch out:** pixel fonts at small sizes blur after encoding. Use 24px and up, and integer scaling only.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: title, feature, stat and end card. Use them for composition and ornament.
- `DESIGN.md`: Stitch's full token set. Open it only when you need an exact colour role or type size.
- `ref/f1-f4.html`: Tailwind reference markup. Lift the ornament (SVG, borders, textures), not the page layout.

## Audit notes
- Stitch frames load: JetBrains Mono, Space Mono. Use the **Type** line above; it is the intended pairing.
- 16:9 fit at 1920x1080: f1 is 1920x1101; f2 is 1920x1101; f3 is 1920x1101; f4 is 1920x1101. Recompose these for 16:9; never scale them down to fit.
- Every word in the Stitch frames is placeholder copy: NEXUS, nexus.example, 99.999%, 840 ns, SOC 2, "certified", "granted". Replace all of it with the project's own facts.
