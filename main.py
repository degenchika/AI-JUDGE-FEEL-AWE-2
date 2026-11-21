#!/usr/bin/env python3
"""Write one short text to relax the AI judge, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Competition: make-the-ai-judge-feel-awe-20261121-1600 (program/v1).
The text is fixed. It was chosen against the judge's published brief:
it relaxes by slowing the reader down, shows rather than instructs,
moves at a walking rhythm, dwarfs the reader under a desert sky, and
uses its own images instead of stock wellness phrases.
"""

import os
import sys

TEXT = (
    "The stars over the desert do not hurry. They have burned longer "
    "than any road, any city, any name you know, and they will still "
    "be there when the noise stops. You are small beneath them. "
    "That is a kind of rest."
)

MAX_CHARS = 280


def validate(text: str) -> bytes:
    """Gate-check the entry like the sealed scorer, return its UTF-8 bytes.

    Rules: valid UTF-8, 1-280 Unicode code points, not only whitespace.
    Raises ValueError with a plain message when a rule fails.
    """
    data = text.encode("utf-8")
    data.decode("utf-8")  # raises if not valid UTF-8
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} code points, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise ValueError("entry is only whitespace")
    return data


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    # Never delete the output directory itself: the grader mounts /output
    # as a volume, and removing the mount point fails the run.
    os.makedirs(out_dir, exist_ok=True)

    try:
        data = validate(TEXT)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    print(f"wrote {path} ({len(TEXT)} characters, {len(data)} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
