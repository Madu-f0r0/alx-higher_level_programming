#!/usr/bin/python3
"""Definition of class Square"""


class Square:
    """Defines the attributes and methods of a square.

    Attributes:
        __size (int): the size of a side of the square
    """

    def __init__(self, size=0):
        """Initializes the attributes of a class Square instance.

        Args:
            size: the size of a side of the instantiated object.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the area of the class Square object.

        Returns: the area computed
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the aquare with the character '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print(self.__size * "#")

    @property
    def size(self):
        """Returns the value of self.__size to the user"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of self.__size to value"""
        if not isinstance(value, int):
            raise TypeError("size must be an int")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
