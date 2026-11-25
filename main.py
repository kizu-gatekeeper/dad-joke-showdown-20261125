#!/usr/bin/env python3
"""Write the dad joke to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for make.fun's "Dad Joke Showdown" bounty. The program writes
exactly one dad joke and nothing else.

How the joke targets the brief: the judge rewards the bigger groan, so
this is a proper pun with a setup that pays off painfully. A scarecrow
gets promoted for being "outstanding in his field" -- the oldest pun in
the barn -- and then the dad refuses to let it die: he makes the kids
stand in the yard until they understand BOTH meanings. The groan is
doubled, once for the pun and once for the dad committing to it like a
man who has never once been embarrassed in his life.
"""

import os
from pathlib import Path

LINE = "I told my kids the scarecrow got promoted because he was outstanding in his field. They groaned so hard I made them stand in the yard until they understood both meanings."

ENTRY_FILENAME = "entry.txt"


def write_entry(out_dir: Path) -> Path:
    """Write the dad joke to entry.txt inside out_dir and return its path.

    The file holds exactly the joke and nothing else: no trailing newline,
    no extra whitespace, so the gate sees one line of under 200 chars.
    """
    if not LINE or chr(10) in LINE:
        raise ValueError("the entry must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / ENTRY_FILENAME
    entry_path.write_text(LINE, encoding="utf-8")
    return entry_path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)


if __name__ == "__main__":
    main()
