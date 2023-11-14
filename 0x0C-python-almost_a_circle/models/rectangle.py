#!/usr/bin/python3

"""Module that defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle
            x (int): The x coordinate of the new Rectangle
            y (int): The y coordinate of the new Rectangle
            id (int): The id of the new Rectangle.
        Raises:
            TypeError: If either width or height is not an int.
            ValueError: If either width or int is < 0
            TypeError: If either x or y is not an int
            ValueError: If either x or y < 0
        """

        if id is not None and not isinstance(id, int):
            raise TypeError("id must be an integer")

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Editing the __str__ method to taste"""
        return (
            "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
            )

    """Defining the getter method for width"""
    @property
    def width(self):
        return self.__width

    """Defining the setter method for width"""
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    """Defining the getter method for height"""
    @property
    def height(self):
        return self.__height

    """Defining the setter method for height"""
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    """Defining the getter method for x"""
    @property
    def x(self):
        return self.__x

    """Defining the setter method for x"""
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    """Defining the getter method for y"""
    @property
    def y(self):
        return self.__y

    """Defining the setter method for y"""
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Prints Rectangle instance with # Character"""
        for i in range(self.height):
            print("#" * self.width)
