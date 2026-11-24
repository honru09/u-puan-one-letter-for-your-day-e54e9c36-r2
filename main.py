"""One Letter for Your Day — round 2.

The letter is D. It stands for "deadline": today's real day was one
deadline after another — radar rounds every thirty minutes, quota checks,
and this very entry racing a 22:26 cutoff. One letter, nothing else.
"""

import os

LETTER = "D"

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def clear_output_dir():
    """Clear /output contents only; never remove the dir itself.

    The grader runs as uid 65534 and cannot remove the root-owned
    mountpoint, so only files inside are removed.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)


def main():
    if len(LETTER) != 1 or not LETTER.isalpha():
        raise ValueError("entry must be exactly one letter A-Z")
    clear_output_dir()
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
