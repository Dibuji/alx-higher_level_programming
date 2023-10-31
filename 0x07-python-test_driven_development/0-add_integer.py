#!/usr/bin/python3
"""Defines addition between integers"""


def add_integer(a, b=98):
    """Function that adds two integers

    Float arguments are casted to int before addition

    Args:
        a (int): first integer
        b (int): second integer

    Raises:
        TypeError: If either of a or b is a non-integer and/or non-float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
