# Transit Map

The user journey drawn as a metro map: stations are steps, and a train runs the route.

- **Best for:** workflows, pipelines, onboarding, integrations, multi-step products
- **Palette:** white `#ffffff`, line colours `#e32017` `#0098d4` `#00782a` `#ffd300`, ink `#1c1c1c`
- **Type:** Albert Sans, geometric and signage-like; station names in uppercase
- **Texture:** clean 45° and 90° lines only, interchange rings, a key panel
- **Signature move:** a train dot runs the line; at each station a platform sign flips to that feature's copy
- **Transitions:** the camera tracks along the line; interchanges switch lines
- **Sound:** station chime (two notes, in key), train rumble, a door-close beep on each beat
- **Watch out:** four stations at most on screen, or it becomes a real map nobody reads.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: title, feature, stat and end card. Use them for composition and ornament.
- `DESIGN.md`: Stitch's full token set. Open it only when you need an exact colour role or type size.
- `ref/f1-f4.html`: Tailwind reference markup. Lift the ornament (SVG, borders, textures), not the page layout.

## Audit notes
- Stitch frames load: Space Grotesk. Use the **Type** line above; it is the intended pairing.
- 16:9 fit at 1920x1080: f1 is 1920x1101. Recompose these for 16:9; never scale them down to fit.
- Sanitised on import: 1x no transit-authority roundel.
- Every word in the Stitch frames is placeholder copy: NEXUS, nexus.example, 99.999%, 840 ns, SOC 2, "certified", "granted". Replace all of it with the project's own facts.
