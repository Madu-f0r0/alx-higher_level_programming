#!/usr/bin/python3
"""Definition for class Square. Getters and setters added."""


class Square:
    """Defines the attributes and methods of the class Square

    Attributes:
        __size (int): the size of a side of an instance of a Square
    """

    def __init__(self, size=0):
        """Initializes the an instance of the class Square.

        Args:
            size (int): the size passed to the object upon
            instantiation.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square object.

        Returns:
            the square calulated
        """
        return self.__size ** 2

    @property
    def size(self):
        """ Returns the size attribute to the user """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size attribute of an object to value.

        Args:
            value (int): the new size of a side of the object square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
