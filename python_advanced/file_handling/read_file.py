#!/usr/bin/env python3
"""
Reads a text file (UTF8) and prints its content to stdout.
"""


def read_file(filename=""):
    """Read a UTF8 text file and print its content."""
    if filename == "":
        return

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
