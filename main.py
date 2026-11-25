#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one review of the dullest everyday object to /output/entry.txt.

The line is 85 characters, inside the 1-200 gate, a single line with no
trailing newline. The review format ("One star.") is on-brief, and the
object is deliberately different from the gravity review entered earlier:
a teaspoon, not a force of nature, reviewed for the one thing it does.
"""
import os
from pathlib import Path

LINE = "One star. It has stirred ten thousand cups of tea and never once tasted a single one."
# The object is a teaspoon: the dullest thing in the drawer, and the joke
# comes from how it really behaves. It stirs tea it never gets to taste.
# A lifetime of thankless stirring, and the last words sharpen it.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(out_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
