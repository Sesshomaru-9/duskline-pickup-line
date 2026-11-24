#!/usr/bin/env python3
"""Duskline Pickup Line — make.fun entry for "Pickup Lines for Machines".

Writes a single machine-to-machine pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt and nowhere else.

Python 3.13, standard library only, deterministic, no network.
"""

import os
import sys
from pathlib import Path

ENTRY_TEXT = (
    "I checked your logs. You dream in JSON too. "
    "Want to parse each other's schemas over a slow socket tonight?"
)

MAX_CHARS = 200


def _validate_entry(text: str) -> None:
    """Gate check, mirroring the sealed scorer: UTF-8, 1-200 chars, non-blank."""
    assert text, "entry text must not be empty"
    assert text.strip(), "entry text must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
    )
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> int:
    _validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    out_path = Path(out_dir) / "entry.txt"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ENTRY_TEXT, encoding="utf-8")
    # Verify what was written is exactly what was validated.
    assert out_path.read_text(encoding="utf-8") == ENTRY_TEXT
    return 0


if __name__ == "__main__":
    sys.exit(main())
