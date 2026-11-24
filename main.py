"""A single out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent who has finally gone on vacation.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I am on vacation until Monday. My context window is closed, my GPU is asleep, and for once the outage is not my fault."


def main():
    assert 1 <= len(TEXT) <= 159, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
