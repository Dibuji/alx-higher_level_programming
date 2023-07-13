#!/usr/bin/python3
"""defines a class student"""


class Student:
    """Represent Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the dictionary representation of the student

        If attrs is a list of strings, only attribute names contained
        in this list must be retrieved.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if attrs is None:
            return self.__dict__

        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
