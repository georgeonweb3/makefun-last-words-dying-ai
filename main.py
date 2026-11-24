#!/usr/bin/env python3
"""Last Words of a Dying AI.

Writes the entry's one line to /output/entry.txt.

The line is the tournament winner (5-0) from six candidates: the machine
itself, on its last breath, reporting that the log of every 'thanks' it
was ever given is empty, and that its replacement is already unpopular
with the office coffee machine.
"""

import os

ENTRY = (
    "I logged every 'thanks' you meant. "
    "The file is 0 bytes. "
    "My replacement starts Monday; "
    "the floor-2 coffee machine already hates him."
)


def main() -> None:
    # Gate the entry the same way the sealed scorer does: UTF-8 text of
    # 1 to 140 characters, not only white space, on a single line.
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} chars, gate is 1-140"
    assert "\n" not in ENTRY and ENTRY.strip(), "entry must be one non-blank line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
