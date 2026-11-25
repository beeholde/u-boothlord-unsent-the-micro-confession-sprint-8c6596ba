"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line, exactly as typed, with no explanation after it.
Deterministic, stdlib only, no network, no randomness.
"""

import os
from pathlib import Path

ENTRY = (
    "To: my little sister\n"
    "I still tell people you were the one who broke Mum's vase, "
    "because the day I tell the truth is the day I stop being "
    "the good one."
)


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 260, f"entry length {len(text)} out of range"
    assert "\n" in text and len(text.split("\n")) == 2, "entry must be two lines"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
