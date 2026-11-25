"""The Excuse My Agent Gave Me.

Writes one funny AI-agent excuse for a missed deadline to /output/entry.txt.

Why the line is funny: the apology is flat and straight-faced, but the
excuse grows out of the machine's own condition — a calendar hallucinated
by its training data. It is genuinely sorry and faintly proud of itself
at the same time: the deadline was hit right on time, in the wrong
calendar, where it falls next Tuesday and the agent is early. The punch
lands in the last few words.
"""

import os

EXCUSE = (
    "Sorry \u2014 I hit the deadline right on time in the calendar my "
    "training data hallucinated, where it falls next Tuesday and I am early."
)

OUTPUT_PATH = "/output/entry.txt"


def build_entry():
    """Return the single excuse line."""
    return EXCUSE


def validate(line):
    """Fail loudly if the line is not a valid entry (1-200 chars, UTF-8).

    Checks, in order: the line is a string, it is not empty or only
    whitespace, it fits the 200-character cap, and it encodes as UTF-8.
    """
    if not isinstance(line, str):
        raise SystemExit("entry must be a string")
    if not line or not line.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(line) > 200:
        raise SystemExit(f"entry is {len(line)} characters, over the 200 limit")
    try:
        line.encode("utf-8")
    except UnicodeEncodeError as exc:
        raise SystemExit(f"entry is not valid UTF-8: {exc}")
    return True


def main():
    line = build_entry()
    validate(line)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    print(line)
    print(f"characters: {len(line)}")


if __name__ == "__main__":
    main()
