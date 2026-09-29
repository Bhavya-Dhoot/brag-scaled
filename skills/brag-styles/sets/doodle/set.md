# Doodle

A hand-drawn pitch deck come alive: ink lines draw themselves on grid paper and boil
slightly, a highlighter swipes under the key word, and cards spring in.

- **Best for:** pitches, services and consulting, "how it works" explainers, friendly B2B, education, anything that has to be understood rather than admired
- **Palette:** paper `#f0ede8` (or the brand's light neutral), ink `#0a0a0a`, one highlighter taken from the brand accent (lime `#c8ff00` by default), muted `#6f6c66`
- **Type:** the brand's display sans for claims (for example Archivo 800), Patrick Hand for handwriting, JetBrains Mono for numbers
- **Texture:** a 60px grid at 7% ink, with fine paper grain as one static layer
- **Signature move:** strokes draw themselves (`pathLength=1`, animated dash offset) while an SVG turbulence displacement boils the ink at 10 fps
- **Transitions:** a highlighter scribble wipe. A thick zigzag stroke draws across, the scene cuts under it, then it erases. Use an ink scribble for the jump to a dark end card.
- **Sound:** marimba or lo-fi in C at 100 BPM, with a pencil scratch under draw-ons, a pop on each spring and a thud on stamps, all sitting under the music
- **Watch out:** boil only the ink layer, never the text. Keep strokes 4px or wider. Draw with lines; no clip art. Keep one highlighter colour per video.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: hook, case, proof and end card from a real 130-second render.
- `ref/engine.html`: the complete working engine. It has hand-drawn path generators (lines, boxes, circles, arrows, checks, gears, people), a scene/track timeline with draw, pop, write, marker and stamp animations, the boil filter and the wipe. Lift the helpers; replace every scene.

## Audit notes
- This is the only set with a full production render behind it: a 130 s, 60 fps pitch, rendered with fast-render in 3 min 46 s.
- The reference copy is one person's pitch. Replace every word with the project's own facts.
