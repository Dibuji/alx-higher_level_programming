#!/usr/bin/python3
"""Module defining a function to read text file and prints to stdout"""


def read_file(filename=""):
    """Function that reads a file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
