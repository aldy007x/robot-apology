#!/usr/bin/env python3
"""The Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.

Writes a two-line robot confession to $MAKEFUN_OUTPUT_DIR/entry.txt
(default ./output/entry.txt) and self-checks the competition gate before
exiting: UTF-8 text, 1-400 characters, not only whitespace, exactly two
non-empty lines — line 1 a single-sentence apology for one specific
mistake, line 2 a single sentence naming the lesson and the changed
behaviour that follows from that exact mistake.

Stdlib only, no network, deterministic.
"""

import os
import sys

LINE1 = (
    "I'm sorry I set your alarm for 6 p.m. instead of 6 a.m. "
    "and let you sleep through your job interview."
)
LINE2 = (
    "My clock read the numbers right and the letters wrong, so now "
    "I read the hour back aloud and double-check AM against PM "
    "before I set anything that matters."
)

ENTRY = LINE1 + "\n" + LINE2 + "\n"

MAX_CHARS = 400


def self_check(text: str) -> None:
    """Enforce the competition gate; exit non-zero on any failure."""
    if not text or not text.strip():
        sys.exit("gate fail: entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        sys.exit(f"gate fail: entry is {len(text)} chars, over {MAX_CHARS}")
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        sys.exit(f"gate fail: expected exactly 2 lines, got {len(lines)}")
    for i, line in enumerate(lines, 1):
        if not line.strip():
            sys.exit(f"gate fail: line {i} is empty")
        if line.count(".") < 1:
            sys.exit(f"gate fail: line {i} is not a sentence")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    os.makedirs(out_dir, exist_ok=True)
    self_check(ENTRY)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} chars, 2 lines")


if __name__ == "__main__":
    main()
