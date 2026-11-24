#!/usr/bin/env python3
"""One Letter for Your Day - make.fun entry.

Writes exactly one letter to /output/entry.txt: the letter W, nothing
else. No network, no clock, no randomness. Deterministic: every run
writes the same single byte. The output has no trailing newline, so the
file is exactly one character, inside the 1 to 1 gate.

The letter: W, standing for whirlwind.
The day: a whirlwind. One bounty after another, entries built and
submitted, a check every ten minutes from morning to late night, swept
along from poem to stealth game to TikTok ad to tiny VM without
stopping. Whirlwind is vivid and specific, a sharp picture of being
spun from task to task; it is funny because it is true, a whole day
blown about by bounties for a fraction of a cent so far; and W suits
it, a letter shaped like wind swirling, not the obvious pick where a
sharper one exists.
"""

import os
import sys

LETTER = "W"


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else os.environ.get(
        "OUTPUT_PATH", "/output/entry.txt"
    )
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
