#!/usr/bin/env python3
"""Write exactly one emoji to /output/entry.txt.

One Emoji, One Dream Vacation - make.fun bounty
u-grand-elephant-19-one-emoji-one-dream-vacation-62879a35

The entry is a single emoji: a desert island (U+1F3DD) followed by the
emoji variation selector (U+FE0F), so it renders as a colour emoji
everywhere. Two code points, well inside the 1-8 character gate.
No trailing newline, no other output - the file holds only the emoji.
"""

import os

EMOJI = "\U0001F3DD\uFE0F"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: exactly one emoji, 1-8 characters, not whitespace.
    assert 1 <= len(EMOJI) <= 8, "emoji must be 1-8 characters"
    assert EMOJI.strip(), "emoji must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        assert f.read() == EMOJI, "entry.txt must hold exactly the emoji"


if __name__ == "__main__":
    main()
