"""Write the competition entry text to the output directory.

Standard library only. Deterministic: the same bytes every run.
"""

import os

TEXT = (
    "The kettle clicked off at 3 a.m.\n"
    "Nobody had touched it.\n"
    "The kitchen was dark, windows shut,\n"
    "and steam rose in one slow ribbon\n"
    "from a full mug on the counter,\n"
    "the tea still turning inside.\n"
    "Beside it, a second spoon waited,\n"
    "clean, unused, in its place.\n"
    "The sugar bowl stood open."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
