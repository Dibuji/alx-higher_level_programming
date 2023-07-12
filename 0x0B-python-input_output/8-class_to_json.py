#!/usr/bin/python3
"""function that defines a class to JSON function"""


def class_to_json(obj):
    """Return the dictionary represntation of a simple data structure."""
     return obj.__dict__
