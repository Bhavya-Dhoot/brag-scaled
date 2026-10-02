---
name: fast-render
description: Render an HTML motion page that exposes window.render(t) to video fast — GPU rasterisation, parallel browsers, frames piped straight to the encoder, hardware H.264 when available. Also exports 4K, transparent ProRes and PNG sequences, lays a page over recorded footage, measures whether a video plays like a slideshow (--audit), and checks the machine's setup (--doctor). Use for every /brag-slim render and any other video drawn frame by frame in a browser (launch videos, animated explainers, motion graphics), for still-frame checks of such a page, and whenever a render is slow, a font is missing or an export format is needed, instead of writing a screenshot loop.
---

# fast-render

Run `scripts/fastrender.py` from this skill's directory. It needs Python 3.9+,
`pip install playwright imageio-ffmpeg`, and `playwright install chromium`.

## Page contract
- `window.render(t)` draws the frame at `t` seconds, as a pure function of `t`.
- `window.ready` is a promise that resolves once fonts and images are loaded.
- `window.DURATION` gives the length in seconds. It is optional if you pass `--duration`.

## Commands
Stills, for checking scenes and mid-transition frames. These are lossless PNGs:
```
python <skill-dir>/scripts/fastrender.py video.html --stills 1.5 7 12.25 --still-dir stills
```
The full render, with the poster baked in as frame 0 and the audio muxed:
```
python <skill-dir>/scripts/fastrender.py video.html --out brag.mp4 --fps 30 --audio score.wav --poster 18.5 --poster-jpg brag.jpg
```

More, each tested on the reference machine:
```
python <skill-dir>/scripts/fastrender.py --doctor                      # what is installed, and is the GPU used
python <skill-dir>/scripts/fastrender.py video.html --audit            # is the picture changing, or is it a slideshow
python <skill-dir>/scripts/fastrender.py video.html --dump-sfx sfx.json   # the page's sound cues, for motion-kit's soundkit
python <skill-dir>/scripts/fastrender.py video.html --out brag-4k.mp4 --scale 2   # 3840x2160 from a 1920x1080 page
python <skill-dir>/scripts/fastrender.py video.html --out small.mp4 --crf 23      # about half the file size
python <skill-dir>/scripts/fastrender.py card.html --transparent --out card.mov --png-dir card-png   # ProRes 4444 with alpha
python <skill-dir>/scripts/fastrender.py overlay.html --over clip.mp4 --out with-graphics.mp4        # graphics over footage
```

## Read the first line it prints
`renderer:` names what drew the frames. If it says **SwiftShader**, Chromium is
rasterising on the CPU and the render will be roughly 10× slower. Tell the user,
since their GPU flags or drivers need attention; the video still renders correctly.

## The checks it makes for you
- A page whose script failed, or whose `window.render` throws on some frame, stops the render with the error. It used to capture a stale frame and carry on.
- `--audit` samples four frames a second and prints the median share of pixels changing, the share of time that is quiet (under 1%), and every quiet stretch of 1.5 s or more. The bottom 14% of the frame is ignored so captions do not pass for action (`--audit-mask-bottom 0` to include it). Two videos a viewer called slideshows measured 52% and 42% quiet; a demo he accepted measured 5%. Fix the listed stretches before rendering.

## Flags worth knowing
- `--scale 2`: re-rasterises at twice the size, so text and edges are sharper, not stretched. Four times the pixels: 2.6 fps per browser measured at 4K.
- `--crf N`: quality, lower is better. It maps onto each encoder's own knob. Grain and noise make large files; 23 roughly halves them.
- `--lufs`: loudness target for `--audio`, default -16; use -14 for YouTube.
- `--transparent`: the page must leave `html` and `body` without a background. Frosted-glass cards have nothing to blur on a transparent page, so use solid ones. `--out` must end in `.mov`.
- `--over clip.mp4`: the footage sets the size, frame rate and length; its audio is kept untouched and `--audio` (sound effects) is mixed under it.
- `--workers N`: parallel browsers. The default is ¾ of the CPU threads, capped at 12.
  Past that point the CPU saturates.
- `--encode-jobs N`: parallel encoder sessions, default 4. Consumer GPUs cap
  hardware sessions. Workstation cards (RTX A-series and similar) can take 12:
  that took the encode on the reference laptop from 80 s to 54 s.
- `--encoder`: `auto` tries NVENC, Quick Sync, AMF, VideoToolbox, then libx264, and
  test-encodes each one before using it. Force one with a name.
- `--capture png`: use it only if JPEG q100 bands a fine gradient. It is about 40% slower.
- `--keep`: keeps the intermediate segments, for debugging.

## Why it is built this way
Measured on Windows 11 with an i9-11950H (16 threads), an RTX A2000 Laptop GPU and an NVMe drive:
- Default headless Chromium rasterised on the CPU at 0.5–1.7 s per 1080p frame.
  On the GPU it took about 75 ms.
- Twelve browsers reached about 45 fps of capture.
- Running NVENC during capture dropped throughput to 17 fps, because it shares
  the GPU. So capture only stream-copies JPEGs, and encoding waits until it is done.
- Converting the JPEG's BT.601 matrix to BT.709 halved encode speed. The script
  converts only the range and tags the matrix. The output decodes within
  43.6 dB PSNR of a lossless capture.
- End to end: a 130 s, 60 fps film took about 45 min with screenshots to disk plus x264.
  It takes 4 min 46 s with the defaults, and 3 min 46 s with `--encode-jobs 12`.

The macOS and Linux GPU flags are the documented ANGLE backends but are not yet
measured. The `renderer:` line tells you what actually ran.
