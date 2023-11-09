#!/usr/bin/python3
"""function that defines a class to JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure."""
    serialized = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[key] = value
    return serialized
