# Glass Layers

Glassmorphism: frosted panels stacked in depth over slowly moving colour.

- **Asked for as:** glassmorphism, frosted glass, glassy, liquid glass, translucent UI
- **Best for:** consumer fintech, AI products, OS-like interfaces, mobile apps. Acceptable for SaaS; weak for operations and finance buyers
- **Palette:** deep `#0B1020` with three drifting colour fields: indigo `#3B2BFF`, teal `#00C2A8`, rose `#FF5C8A`; glass is white at 12% with a 1 px white 30% edge; text white
- **Type:** Inter 700 and 400; Space Grotesk 700 for numbers
- **Texture:** frosted panels (`backdrop-filter: blur(24px)`) stacked in depth, a brighter top edge on each, colour moving behind them
- **Signature move:** rack focus. Panels slide over the moving colour; the active one comes forward and sharpens while the others drop back, shrink and dim
- **Transitions:** the front panel grows until its frost fills the frame, then clears
- **Sound:** a soft pad and airy clicks; `pulse` bed at low gain; `click`, `switch`, `chime`
- **Watch out:** backdrop blur is the slowest thing to render: no more than four frosted panels on screen. Put a dark scrim behind any text on glass. Over transparent footage there is nothing to blur, so use solid cards there

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: the hook, the signature move mid-way, the proof, the end card.
- `ref/look.html`: a ten-second working sample of this look: the entrance, the signature move with a performer, a counted proof and the end card, every frame a pure function of time. Lift the mechanism; replace every word and number. It loads fonts from `../../../../motion-kit/fonts/`.
