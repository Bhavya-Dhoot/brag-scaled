# Brutal Bento

A loud personal intro: a boring page gets smashed, a neo-brutalist bento board assembles behind
it, and the camera dives into its tiles, each one a room where something is operated.

- **Best for:** personal intros, creators, developer tools, hiring posts, anything that should feel made by a builder; a 20 to 30 second film with a scannable call to action. Not for conservative finance or enterprise buyers, who read heavy neo-brutalism as less trustworthy: use `ops-desk` there
- **Palette:** paper `#FDFBF6`, ink `#000`, and three neons used as fills behind black text, never as text on paper: lime `#32FF00` (done), cyan `#00FFFF`, magenta `#FF00FF`; hazard yellow `#FFD400` for coins and rewards. One room goes black with lime type
- **Type:** Archivo Black in capitals for everything loud, with a 12 px black outline and a hard offset shadow on headline words; JetBrains Mono for labels and data; Space Grotesk 700 for captions
- **Texture:** 6 px black borders, 10 px hard shadows, no radius, no gradients; a dot grid in the light room and falling code in the dark one; pixel art for the portrait and the mascots
- **Signature move:** a cursor in a hard hat smashes a résumé into shards on the second beat; the board behind it is made of live miniatures, and the camera flies into one until it fills the frame. At the end every tile folds into a QR code that then sits still
- **Transitions:** camera only. Fly into a tile, whip sideways to the next, pull back out; a white flash and a glitch on the two hard hits
- **Sound:** two beats of lift music cut off by breaking glass, then the `phonk` bed at 140 BPM, which stops dead on the last hit: `soundkit.py sfx.json --out score.wav --bed phonk --bpm 140 --t0 0.857 --tail 2.57` (`--t0` is the smash, `--tail` is the time from the last hit to the end). Cues from the louder set: `shatter slam cash coins payout lock ratchet ping squawk quack boom`
- **Watch out:** wall-to-wall jokes hide the message, so every room still ends on one plain claim in large type. Keep neon off small text. The QR code must be flat, still and uncovered for at least three seconds, and checked with `qr.py --check` on a frame from the encoded video

## Reference kit (open only what you need)
- `frames/f1-f4.webp`: the smash headline, the reward frame in the light room, the dark room, the end card.
- `ref/engine.html`: the complete working film: shards, tiles that pop in and later fold away, rooms scaled into tiles, camera and cursor keys, an indexing conveyor, a readout that falls through units, meshing gears, the QR assembly, captions. Every time in it is in beats.
- `ref/scenes.json` and `ref/layout.js`: each narration line placed on a beat with `at` (`motion-kit/scripts/fit_scenes.py` wrote the layout from the spec).
- `ref/qr.js`: the module grid from `motion-kit/scripts/qr.py`.
- The fonts load from `../../../../motion-kit/fonts/`; copy that folder beside your page and change the link.

## Audit notes
- Activity audit on the reference: median 8.0%, quiet 9% of the time, no quiet stretch of 1.5 s.
- A 15 second brief with five scenes and a narrator does not fit: about 55 spoken words is 19 s of voice. This reference runs 60 beats (25.7 s) with a line on almost every bar.
- The reference copy is one person's pitch. Replace every word and every number, and show only figures you can stand behind.
