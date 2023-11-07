#!/usr/bin/python3
"""Defines a lookup function for an object"""


def lookup(obj):
    """Function that returns list of available attributes and methods"""

    return dir(obj)
