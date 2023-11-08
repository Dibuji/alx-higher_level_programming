#!/usr/bin/python3
"""Module defining a function to write a string to a text file"""


def write_file(filename="", text=""):
    """Function that reads a file"""

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
