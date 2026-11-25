#!/usr/bin/env python3
"""Worst Superpower entry: an elevator hero with perfect timing.

Prints nothing; writes the one-line superpower to /output/entry.txt.
Standard library only, deterministic, no network, no secrets.
"""
from pathlib import Path

ENTRY_TEXT = (
    "I can summon any elevator instantly \u2014 by pressing the button "
    "after the doors open and taking full credit."
)


def write_entry():
    """Write the entry line to the grader's output path."""
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
