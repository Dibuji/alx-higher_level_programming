#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    unless its 'first_name'
    """

    __slots__ = ["first_name"]
