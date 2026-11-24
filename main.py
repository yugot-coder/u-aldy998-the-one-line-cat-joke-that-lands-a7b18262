"""The One-Line Cat Joke That Lands -- make.fun entry (program/v1,
Python 3.13, stdlib only).

Writes one joke about cats, a single line under 200 characters, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output/entry.txt``).

The joke is picked from CANDIDATES by SELECTED. The winner was chosen
against the judge brief: a setup and a turn that lands, a surprise
rather than a heard-it-before pun, tight, and retellable. The winner
flips the usual frame -- the cat is not the pet being reviewed, the
human is the one underperforming -- and the punchline is the last word.
"""

import os

MAX_CHARS = 199  # the brief says under 200 characters

CANDIDATES = (
    # The cat out-types the human.
    "My cat knocked my laptop off the table, sat on the keyboard, and "
    "typed a better password than any I've ever chosen.",
    # The $90 bed loses to its box; rent is paid in broken glasses.
    "I bought my cat a $90 bed; she sleeps in the box it came in and "
    "charges me rent in knocked-over glasses.",
    # 3 a.m. meowing as a mercy, not a demand.
    "My cat doesn't meow at 3 a.m. to be fed -- she meows to remind me "
    "she could have been a tiger and chose mercy.",
    # Sit training, applied everywhere except the target.
    "I trained my cat to sit. Now she sits -- on my laptop, my book, "
    "my face -- anywhere except where I trained her.",
    # An hour of wall-staring, judged back.
    "My cat stared at the wall for an hour, then looked at me like I "
    "was the one wasting time.",
    # The vet is lucky the exam table has no edge.
    "The vet said my cat is overweight. My cat said the vet is lucky "
    "the exam table has no edge to push him off.",
    # WINNER: the cat's performance review of the human.
    "My cat brings me dead mice because in her performance review, "
    "I'm the one underperforming.",
    # Exactly one square of the bed, the occupied one.
    "I asked the cat for space. She gave me exactly one square of "
    "the bed -- the one my feet were on.",
)

SELECTED = 6


def main() -> None:
    line = CANDIDATES[SELECTED]
    if not line or line.strip() != line:
        raise SystemExit(
            "selected line must be non-empty with no surrounding whitespace"
        )
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(line)} characters, over the {MAX_CHARS} cap"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    # Verify what landed on disk is exactly the chosen line.
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("entry.txt on disk differs from the chosen line")
    print(f"wrote {len(line)} characters to {path}")


if __name__ == "__main__":
    main()
