#!/usr/bin/python3
"""Defines a function that checks inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (object): Object to be checked
        a_class (type): The class to be checked against
    Returns:
        If obj is an inherited instance of a_class - True
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
