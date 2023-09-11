#!/usr/bin/python3
""" This module contains the definition of a class Square.

This class is derived from the base class Rectangle from
module 9-rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines the the methods and attributes of class Square.

    It is a derived class of the class Rectangle
    Attribute:
        @__size: the dimension of the Square instance
    """

    def __init__(self, size):
        """ Initializes the size of a Square instance.

        Args:
            @size (int): the value to initialize @__size
        """

        self.integer_validator('size', size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    def __str__(self):
        """Returns a representation of a Square object"""

        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
