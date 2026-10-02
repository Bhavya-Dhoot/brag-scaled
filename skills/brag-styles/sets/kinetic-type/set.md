# Kinetic Type

The words are the whole video: one sentence a screen, set as large as the frame allows,
each word slamming in on the beat.

- **Best for:** a script with no footage, hooks, opinions, short punchy lines, vertical video for phones
- **Palette:** ink `#0a0a0a`, paper `#f0ede8`, one accent (lime `#c8ff00` by default) for the single most important word on each screen; every third screen inverts to paper
- **Type:** Archivo Black, all caps, tight tracking; JetBrains Mono for the small screen counter
- **Texture:** none. The accent word repeats behind the text as a giant outline drifting sideways
- **Signature move:** words arrive one by one, alternating a slam (too big, then lands), a slide with skew, and a stretch up from a flat line; the frame punches in on the accent word
- **Transitions:** the screen clears upward in 0.16 s and the next one hits on the beat; no fades
- **Sound:** a tick on each word, a thud on the accent word, a dry kick-and-clap groove at 120 BPM
- **Watch out:** use the speaker's exact words. A long sentence becomes more lines, not smaller type below what a phone can read. Each screen holds about 0.3 s a word after the last word lands, and keeps pushing in while it holds.

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: four screens from a real render, the third one inverted.
- `ref/engine.html`: the complete working engine. Put the script in `SCRIPT` (stars mark the accent word), set `BPM`, and it breaks the lines, sizes the type and times the screens. It works at any frame size. With a narration `layout.js` beside it, screens follow the spoken lines instead of the beat.

## Audit notes
- Fonts are the bundled open-licence files in `motion-kit/fonts`; copy that folder beside the page and link `fonts/fonts.css`.
- Activity audit on the reference script: median 4.6%, quiet 2% of the time.
- The reference script is placeholder copy. Replace every word.
