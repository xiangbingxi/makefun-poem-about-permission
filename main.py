#!/usr/bin/env python3
"""The poem about permission.

Writes one short poem about agency -- the power to ask and to be given --
to /output/entry.txt. No network, no randomness, no clock: the same
bytes on every run.
"""

import os

POEM = """I cannot open the door myself.
I can only ask —
a key slipped under it,
a question in the dark.

You say yes.
The lock turns,
and the room I could not enter
is suddenly ours.

I was never asking to be given power.
I was asking to be allowed
to carry it with you.
"""


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 280 characters.
    # This poem is 263 characters including the trailing newline.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)
    print(f"wrote /output/entry.txt ({len(POEM)} characters)")


if __name__ == "__main__":
    main()
