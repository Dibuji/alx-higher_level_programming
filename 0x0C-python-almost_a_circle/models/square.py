#!/usr/bin/python3
"""Module that defines a Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square Class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Defines the str method for the Square Class"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
