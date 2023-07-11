#!/usr/bin/python3
"""Function for reading a file."""


def read_file(filename=""):
    """Read the contents of a UTF8 text file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
