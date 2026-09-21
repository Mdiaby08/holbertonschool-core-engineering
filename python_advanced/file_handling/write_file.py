#!/usr/bin/env python3
"""
Write a function that writes a string to a text file (UTF-8) and returns the number of characters written:
"""

def write_file(filename="", text=""):
    """Writes a string to a text file (UTF-8) and returns the number of characters written"""
    if filename == "":
        return

    with open(filename, "r", encoding="utf-8") as f:
        print(f.write()(), end="")
