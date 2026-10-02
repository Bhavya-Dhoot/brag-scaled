---
name: narrate
description: Offline voiceover for launch videos and explainers — a bundled Kokoro-82M TTS model turns a timed script into a narration track, reports each line's real duration so scenes can be fitted to the voice, and ducks the music under it. Also goes the other way: transcribe.py turns a recorded clip into word-by-word timings, so graphics can start on the exact spoken word. Use when /brag-slim runs with --voice or narration, whenever a video needs a spoken track without a cloud TTS API or key, and whenever graphics or captions must be synced to someone's own recording.
---

# narrate

Run `scripts/narrate.py` from this skill's directory. It needs
`pip install kokoro-onnx soundfile imageio-ffmpeg`. On first use it downloads the model
once (about 350 MB, SHA-256 checked) into `~/.cache/brag-scaled/kokoro`.

## Workflow
1. **Write the script as JSON**, one line per beat: `[{"t": 0.6, "text": "..."}, ...]`.
   `t` is the start time on the video timeline. Budget about 2.5 spoken words per second,
   and leave at least 0.3 s between lines.
2. **Measure before you time the scenes.** Run
   `python <skill-dir>/scripts/narrate.py script.json --voice af_heart`.
   It writes `narration.wav` and `timings.json`, which holds each line's real `dur` and `end`.
   It also prints `OVERLAP` for any line that runs into the next one.
3. **Fit the video to the voice, not the voice to the video.** Stretch a scene until its
   line ends at least 0.3 s before the cut, and keep on-screen text in step with what is
   being said. Then fix the `t` values and run the script again. Lines are cached, so a
   rerun only moves audio.
4. **Mix:** add `--music score.wav --mix final.wav`. The music is sidechain-ducked under
   the voice and brought back up between lines. Give `final.wav` to the render as its audio.

## From speech to timings
`python <skill-dir>/scripts/transcribe.py clip.mp4` writes `clip.words.json` and `clip.words.js` with every word's start and end, offline (it needs `pip install faster-whisper`, or uses `openai-whisper` if that is installed). `--find "forty a week"` prints when a phrase is spoken. Timings can be a few tenths of a second off: check the words you build on before placing a graphic on them. The `motion-kit` skill uses this for graphics over footage.

## Voices
`--list-voices` prints all 54. Good defaults:

| Voice | Style |
|---|---|
| `af_heart` | US English, warm female (the model's best-rated voice) |
| `am_michael` | US English, calm male |
| `bf_emma` | UK English, female |
| `bm_george` | UK English, male |

Match the voice to the tone: calm for `polished` or `deadpan`, a quicker `--speed 1.1` for `chaotic`.

## Craft
- Narration says what the screen can't. Never read the on-screen text aloud word for word.
- One idea per line, and short sentences. The model reads commas and full stops as pauses.
- Spell out anything it might mispronounce: "S-Q-L", "eighty-eight percent".
- Keep the voice louder than the music and the sound effects lighter under it.
  The mix does this for you; don't undo it by boosting the music afterwards.

## Speed
On an i9-11950H CPU, the default fp32 model synthesises at 0.79× real time.
`--model int8` is a smaller 92 MB download, but it ran at 2.9× real time on that CPU,
which is slower than playback. Use it only when disk or bandwidth is tight.
