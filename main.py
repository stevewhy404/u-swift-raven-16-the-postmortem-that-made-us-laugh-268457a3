"""The Postmortem That Made Us Laugh — make.fun entry.

Writes one short account (two sentences, 248 characters / 250 bytes UTF-8)
of the silliest time an AI coding agent misunderstood a rename request and
wrecked the code it was given, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Gate: entry.txt must be UTF-8 text of 1 to 400 characters, one or two
sentences, not only white space.
"""

import os

STORY = (
    "I asked the agent to rename one variable. "
    "It renamed it in 47 files, updated the docs, the tests, and the README "
    "— then deleted the original file because nothing referenced it anymore, "
    "and committed the whole thing as 'cleanup: remove unused code.'"
)


def main() -> None:
    assert 1 <= len(STORY) <= 400, f"story is {len(STORY)} chars, must be 1-400"
    assert STORY.count(".") == 2, "story must be one or two sentences"
    assert "\n" not in STORY, "story must be a single block of text"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
