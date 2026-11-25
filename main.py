#!/usr/bin/env python3
"""Write one short rant to /output/entry.txt for the Angry Judge contest."""

import os
from pathlib import Path

RANT = (
    "I scanned twelve items. Twelve. Then the self-checkout announced "
    '"unexpected item in the bagging area" to the queue, like I had smuggled '
    "a live goat past security. The unexpected item is my bag: four grams of "
    "plastic, in the bagging area, doing bagging. Now a human must type a "
    "secret code to forgive my groceries. Honestly, arrest me and let me pay "
    "bail with the loyalty card."
)

assert 1 <= len(RANT) <= 400, "rant must fit the 1-400 character gate"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
