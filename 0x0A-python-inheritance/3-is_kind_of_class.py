#!/usr/bin/python3
"""Defines a function that checks object Inheritance"""


def is_kind_of_class(obj, a_class):
    """returns True or False accordingly

    Args:
        obj (object): Object to be checked
        a_class (class): Class to be checked against
    """
    if isinstance(obj, a_class):
        return True
    return False
