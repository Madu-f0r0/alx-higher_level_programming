#!/usr/bin/python3
"""This module contains the definition of the class Square.

class Square is a sublass of class Rectangle in
module models.rectangle
"""

from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the attributes and methods of the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes the attributes of an instantiated Square class.

        Args:
            size (int): the dimension of the square instance
            x (int): number of whitespaces on the x axis of the
            graphically represented square
            y (int): number of whitespaces on the y axis of the
            graphically represented square
            id (int): the id of the Square instance
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the value of @size"""
        return self.height

    @size.setter
    def size(self, value):
        """Sets @size to a given @value"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a formatted representation of a Square instance"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width)

    def update(self, *args, **kwargs):
        """Updates the  values of a Square instance attributes"""
        attributesList = ["id", "size", "x", "y"]

        for i in range(len(args)):
            setattr(self, attributesList[i], args[i])

        if not args or not (args and len(args)):
            for kwarg in kwargs:
                setattr(self, kwarg, kwargs.get(kwarg))

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""
        dict_tuple = (("id", self.id), ("size", self.width),
                      ("x", self.x), ("y", self.y))

        return {x: y for x, y in dict_tuple}
