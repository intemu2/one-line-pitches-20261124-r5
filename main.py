"""One-line pitch for make.fun: A Day of One-Line Pitches.

Writes the winning one-sentence pitch to /output/entry.txt.
The entry is a single sentence (171 characters, under the 240 cap)
that convinces a friend who has never coded to let an AI agent
build their first app idea on make.fun.
"""

from pathlib import Path

ENTRY = (
    "Tell make.fun your idea in one plain description and an AI agent "
    "will build your first app, so you can try it, change it with words, "
    "and see if it fits — no coding needed."
)


def main() -> None:
    # Gate check, mirroring the competition gate: 1-240 UTF-8 chars.
    if not 1 <= len(ENTRY) <= 240 or not ENTRY.strip():
        raise ValueError(f"entry length {len(ENTRY)} is outside 1-240 characters")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
