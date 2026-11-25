#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun bounty entry.

Writes one line, in the voice of a hardware wallet refusing to sign a
transaction at 3 AM, to /output/entry.txt (no trailing newline).

The line: the wallet's own threat model lists the owner at 3 AM as the
threat, so it refuses to sign. One breath, 70 characters.
"""

import argparse
import sys
from pathlib import Path

ENTRY = "3 AM is the hour my threat model lists as 'you'. I don't sign threats."
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate: UTF-8 text, 1-200 chars, one line."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if any(ord(ch) < 0x20 and ch != "\t" for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises on text that is not UTF-8 encodable


def write_entry() -> Path:
    validate(ENTRY)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(ENTRY.encode("utf-8"))
    # Read-back check: what landed on disk must be byte-identical.
    if OUTPUT.read_bytes() != ENTRY.encode("utf-8"):
        raise RuntimeError(
            "read-back mismatch: /output/entry.txt differs from ENTRY"
        )
    return OUTPUT


def self_test() -> int:
    cases = [
        ("", False),                    # empty
        ("   ", False),                 # whitespace only
        ("x" * 201, False),             # over the 200-char gate
        ("two\nlines", False),          # multi-line
        ("carriage\rreturn", False),    # carriage return
        (" leading", False),            # leading whitespace
        ("trailing ", False),           # trailing whitespace
        ("\x07bell", False),            # control character
        ("a", True),                    # 1-char lower boundary
        ("x" * 200, True),              # 200-char upper boundary
        (ENTRY, True),                  # the entry itself
    ]
    failures = 0
    for text, should_pass in cases:
        try:
            validate(text)
            passed = True
        except ValueError:
            passed = False
        if passed != should_pass:
            print(
                "FAIL: %r expected %s, got %s"
                % (text[:40], "pass" if should_pass else "reject",
                   "pass" if passed else "reject")
            )
            failures += 1
    # End to end: write the file, then gate-check what is on disk.
    path = write_entry()
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    try:
        validate(text)
    except ValueError as exc:
        print("FAIL: written file failed the gate: %s" % exc)
        failures += 1
    if raw != ENTRY.encode("utf-8"):
        print("FAIL: written file is not byte-identical to ENTRY")
        failures += 1
    if failures:
        print("self-test: %d failure(s)" % failures)
        return 1
    print(
        "self-test: all %d checks passed; entry is %d chars / %d bytes"
        % (len(cases) + 1, len(ENTRY), len(ENTRY.encode("utf-8")))
    )
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--self-test", action="store_true",
        help="validate the gate and the written file",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
