#!/usr/bin/python3
"""defines a function that checks instance of a class"""


def is_same_class(obj, a_class):
    """Function that returns True or False.

    Args:
        obj (any): Object to be checked
        a_class (type): class to be checked against
    """
    if isinstance(obj, a_class):
        return True
    return False
