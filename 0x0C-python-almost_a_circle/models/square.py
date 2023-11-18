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

    @property
    def size(self):
        """Getter for size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Method that assigns arguments to attributes"""
        if args:
            """Update using non-keyworded arguments if they exist"""
            attributes = ['id', 'size', 'x', 'y']
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)

        elif kwargs:
            """Update using keyword arguments if no args exist"""
            for key, value in kwargs.items():
                setattr(self, key, value)
