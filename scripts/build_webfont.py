# /// script
# requires-python = ">=3.10"
# dependencies = ["fonttools[woff]==4.60.1", "brotli==1.1.0"]
# ///
"""Compress the complete source font; never subset or change shaping data."""

import argparse
from io import BytesIO
from pathlib import Path

from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "Paramita.ttf"
OUTPUT = ROOT / "web" / "Paramita.woff2"


def build() -> bytes:
    with TTFont(SOURCE, recalcTimestamp=False) as font:
        # A signature on the original binary cannot authenticate a new container.
        if "DSIG" in font:
            del font["DSIG"]
        font.flavor = "woff2"
        buffer = BytesIO()
        font.save(buffer)
        return buffer.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check the committed artifact without writing.")
    args = parser.parse_args()
    result = build()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_bytes() != result:
            parser.exit(1, "Web font is missing or stale. Run uv run scripts/build_webfont.py\n")
        print("Web font matches the reproducible build.")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_bytes(result)
    size = SOURCE.stat().st_size
    print(f"{size:,} bytes TTF -> {len(result):,} bytes WOFF2 ({1 - len(result) / size:.1%} smaller)")


if __name__ == "__main__":
    main()
