#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """function to append string to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
