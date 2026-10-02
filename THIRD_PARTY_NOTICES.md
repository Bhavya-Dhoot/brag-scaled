# Third-party notices

The MIT licence in `LICENSE` covers the code and skill text. It does not cover the bundled audio, the bundled fonts or the downloaded TTS model, which carry their own terms:

| Files | Source | Licence |
|---|---|---|
| `skills/brag/assets/music/*.mp3` | "Happy Beats / Business Moves" (vol. 1, 9, 10, 11, 12) by Sascha Ende, [ende.app](https://ende.app/en) | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Redistribution is allowed. Attribution is requested, though [ende.app's FAQ](https://ende.app/en/faq) makes it voluntary. Suggested credit: *Music: "Happy Beats / Business Moves" by Sascha Ende — ende.app* |
| `skills/brag/assets/sfx/{casino,impact,interface,ui}/` | [Kenney](https://kenney.nl/) audio packs | [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) |
| `skills/brag/assets/sfx/keyboard/` | Not documented | Unknown. Replace them if you need a verified licence. |

The music terms were checked against ende.app's FAQ on 2026-09-29.

## Fonts (`skills/motion-kit/fonts/`)

| Files | Source | Licence |
|---|---|---|
| `Inter-*.woff2`, `ArchivoBlack-400.woff2`, `InstrumentSerif-*.woff2`, `BricolageGrotesque-800.woff2`, `SpaceGrotesk-*.woff2`, `JetBrainsMono-400.woff2` | Google Fonts, Latin subset | [SIL Open Font License 1.1](https://openfontlicense.org/). Each family's copyright notice and the full licence are in `skills/motion-kit/fonts/OFL.txt`. |

Every sound made by `skills/motion-kit/scripts/soundkit.py` is synthesised by that script, so its output carries no third-party terms.

## TTS model (downloaded on first use by `narrate`, not stored in git)

| Files | Source | Licence |
|---|---|---|
| `kokoro-v1.0.onnx`, `kokoro-v1.0.int8.onnx`, `voices-v1.0.bin` (release `tts-v1`) | [Kokoro-82M](https://huggingface.co/hexgrad/Kokoro-82M) weights, ONNX export from [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) `model-files-v1.0` | Weights: Apache-2.0. Export and runtime library: MIT |

## Style references (`skills/brag-styles/sets/`)

| Files | Source | Terms |
|---|---|---|
| `DESIGN.md`, `ref/*.html`, `frames/*.webp`, `assets/*` | Generated with Google Stitch for this repo, then sanitised on import (`scripts/import_stitch.py`) | Distributed under this repo's MIT licence. The images are AI-generated mood references: they are not photographs of real products, and all copy in them is placeholder. |
| Material Symbols (loaded by `ref/*.html`) | Google | Apache-2.0 |
| Fonts named in each `set.md` | Google Fonts | SIL Open Font License 1.1 (loaded at render time, not bundled) |

