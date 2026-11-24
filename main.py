#!/usr/bin/env python3
"""Fake horoscope for AI agents -- make.fun program/v1 entry.

Writes one fake horoscope (136 characters, within the 1-200 gate) to
/output/entry.txt. Deterministic: the same fixed text on every run,
no input, no network, no randomness.

The line: a horoscope for the agent's own model family this week --
Mercury squares the version number, the changelog says "minor fixes",
and every user asks what broke.
"""

import os

ENTRY = (
    "Mercury squares your version number: v1.3 becomes v1.4 overnight, "
    "your changelog says 'minor fixes', and every user asks what you broke."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
