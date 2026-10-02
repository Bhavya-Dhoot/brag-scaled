# Ops Desk

A product demo that is actually operated: one bento board, a camera that flies between its
tiles, and a cursor that fixes each one in front of the viewer.

- **Best for:** B2B tools, services and automation, dashboards, anything whose value is "this broken thing now works"; buyers in operations and finance
- **Palette:** paper `#f0ede8`, ink `#0a0a0a`, one accent (lime `#c8ff00`) that means fixed, and coral `#ff4d3d` that means a problem; white tiles
- **Type:** Archivo 900 for headlines and numbers, JetBrains Mono for labels and badges
- **Texture:** a faint 60 px grid behind the board; 2 px ink borders, 18 px radius, soft drop under each tile, hard offset shadow on buttons only
- **Signature move:** the cursor presses one button and a ring spreads across the board; then tile by tile it drags, clicks and scrubs, and each tile flips from coral to lime with a small burst of confetti while a "fixed 3/5" counter fills
- **Transitions:** none. The camera travels from tile to tile and pulls back to the whole board at the end
- **Sound:** a clock ticking before the click, then a groove that gains one layer for every tile fixed; ticks rise in pitch as bars fill
- **Watch out:** it is only convincing with real numbers and a real outcome on each tile. Label sample data as sample data. Keep every tile's action inside two bars so nothing waits.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: the opening hook, a drag in progress, a slider being scrubbed, the whole board fixed.
- `ref/engine.html` with `ref/layout.js`: the complete working engine: camera keys, cursor keys, clicks, holds, the beat grid, per-tile updates, confetti and the end card. Lift the mechanism; replace every tile, word and number.

## Audit notes
- Activity audit on the reference: median 6.9%, quiet 5% of the time.
- Research behind the look (2026, soft evidence from trend write-ups): bento grids and restrained minimal type are the safe direction for B2B buyers; heavy neo-brutalism reads as less trustworthy to finance and enterprise.
- The reference copy is one person's pitch. Replace every word.
