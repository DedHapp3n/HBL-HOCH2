#!/usr/bin/env python3
"""Validate bootstrap.txt against the Pico AutoTyper's US keyboard character set."""

from pathlib import Path

FILE = Path(__file__).with_name("bootstrap.txt")

supported = set(
    "\r\n\t "
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    "0123456789"
    "-=[]\\;'\x60,./"
    "!@#$%^&*()_+{}|:\"~<>?"
)

text = FILE.read_text(encoding="utf-8")
bad = [(i, ch, ord(ch)) for i, ch in enumerate(text) if ch not in supported]

print(f"File: {FILE.name}")
print(f"Characters: {len(text)}")
print(f"Lines: {text.count(chr(10)) + (0 if text.endswith(chr(10)) else 1)}")
print(f"Bytes UTF-8: {len(text.encode('utf-8'))}")

if bad:
    print("\nUNSUPPORTED CHARACTERS:")
    for i, ch, cp in bad[:50]:
        print(f"  offset {i}: {ch!r} U+{cp:04X}")
    raise SystemExit(1)

print("Validation: OK - all characters are supported by the US HID map.")
