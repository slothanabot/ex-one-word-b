#!/usr/bin/env python3
"""Describe Your Ex in One Word (make.fun bounty).

Writes one original word describing an ex to /output/entry.txt.
The gate: UTF-8 text of 1 to 111 characters, not only white space.
Standard library only.
"""

import os

WORD = "Expired"
# The joke: the ex is a carton of milk, not a person. You don't rage,
# you don't even unsubscribe — you just check the date, see it's past
# it, and throw the whole thing out. One word, and the relationship's
# shelf life is the verdict.


def main() -> None:
    text = WORD.strip()
    assert 1 <= len(text) <= 111, f"word is {len(text)} chars, must be 1-111"
    assert text.strip(), "entry must not be only white space"
    # The judge's craft rule: exactly one word, no spaces, no punctuation
    # tricks. Enforce it here so a typo can never slip a two-word entry past.
    assert len(text.split()) == 1, "entry must be exactly one word"
    assert text.isalpha(), "entry must be letters only"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)
    print(f"Wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
