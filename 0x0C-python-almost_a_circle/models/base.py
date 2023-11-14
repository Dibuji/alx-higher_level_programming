#!/usr/bin/python3

"""Module defining the base class"""


class Base:
    """The Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """initialize a new Base

        Args:
            id (int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
