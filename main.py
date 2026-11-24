"""Write one original one-line joke about cats to entry.txt.

Deterministic: the same joke, byte for byte, on every run.
No randomness, no network, no clock, no input files.
"""

import os

JOKE = "My cat brings me the same dead mouse every morning, and I've stopped saying thanks \u2014 I'm pretty sure I'm on a subscription I never signed up for."


def main():
    # Gate self-check: the scorer needs 1-200 characters, one line.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert "\n" not in JOKE, "joke must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
