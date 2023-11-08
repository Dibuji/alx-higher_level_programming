#!/usr/bin/python3
"""Module containing function to append string at end of text file"""


def append_write(filename="", text=""):
    """Function to append string at the end of text file
        Returns number of characters added
    """

    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
