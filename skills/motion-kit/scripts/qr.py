"""A QR code a video can show and a viewer can actually scan.

    python qr.py https://example.com --out qr.js     # window.QR = ["1110...", ...]: one string a row, "1" is a dark module
    python qr.py --check frame.png                   # decode a frame: prints what a phone would read, exits 1 if nothing

The page draws each "1" as a solid dark square on a light card, with four modules of empty
margin on every side. Animate it in however you like, then hold it dead still, flat and
uncovered for the last three seconds: a code that rotates, glows or is built from texture
does not scan. Always run --check on a frame pulled from the encoded video, not from the page.

Requires: pip install opencv-python numpy
"""
import argparse, json, pathlib, sys
import cv2, numpy as np


def grid(text):
    p = cv2.QRCodeEncoder_Params(); p.correction_level = cv2.QRCODE_ENCODER_CORRECT_LEVEL_M
    dark = cv2.QRCodeEncoder.create(p).encode(text) < 128
    rows, cols = np.where(dark.any(1))[0], np.where(dark.any(0))[0]
    core = dark[rows[0]:rows[-1] + 1, cols[0]:cols[-1] + 1]
    run = 0                                                   # the finder's top bar is seven modules wide
    while core[0, run]:
        run += 1
    m = run // 7; g = core[m // 2::m, m // 2::m]
    big = np.kron(np.pad(~g, 4, constant_values=True).astype(np.uint8) * 255, np.ones((12, 12), np.uint8))
    if cv2.QRCodeDetector().detectAndDecode(big)[0] != text:
        sys.exit("the generated code did not decode back to the text")
    return g


def main():
    ap = argparse.ArgumentParser(description="Make a scannable QR module grid, or check a frame.")
    ap.add_argument("text", nargs="?")
    ap.add_argument("--out", default="qr.js")
    ap.add_argument("--check", help="an image to decode")
    a = ap.parse_args()
    if a.check:
        got = cv2.QRCodeDetector().detectAndDecode(cv2.imread(a.check))[0]
        print(got or "no QR code found"); sys.exit(0 if got else 1)
    if not a.text:
        ap.error("give the text to encode, or --check IMAGE")
    g = grid(a.text)
    pathlib.Path(a.out).write_text("window.QR = " + json.dumps(["".join("1" if c else "0" for c in r) for r in g]) + ";", encoding="utf-8")
    print(f"{g.shape[0]}x{g.shape[0]} modules -> {a.out}")


if __name__ == "__main__":
    main()
