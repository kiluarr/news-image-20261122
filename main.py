"""Entry program for make.fun news-image-20261122.

Copies the pre-drawn front page (entry.png, in this repository) to
$MAKEFUN_OUTPUT_DIR/entry.png, after checking the file is a whole,
1024x1024 PNG of at most 1 MiB. Standard library only, no network,
no randomness, no clock: every run writes identical bytes.
"""

import os
import struct
import sys
from pathlib import Path

MAX_BYTES = 1048576
WANTED_WIDTH = 1024
WANTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("main.py: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_png(data):
    """Return (width, height) if data is a complete PNG, else fail."""
    if len(data) > MAX_BYTES:
        fail("entry.png is %d bytes, over the 1048576 limit" % len(data))
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        fail("entry.png is not a PNG file")
    if len(data) < 33 or data[12:16] != b"IHDR":
        fail("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (WANTED_WIDTH, WANTED_HEIGHT):
        fail("entry.png is %dx%d, expected 1024x1024" % (width, height))
    if len(data) < 12 or data[-8:-4] != b"IEND":
        fail("entry.png has no IEND chunk")
    return width, height


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        fail("entry.png not found beside main.py")
    data = source.read_bytes()
    check_png(data)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or ".")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    target.write_bytes(data)
    print("wrote %s (%d bytes, 1024x1024)" % (target, len(data)))


if __name__ == "__main__":
    main()
