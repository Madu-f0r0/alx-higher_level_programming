#!/usr/bin/python3
"""Definition of class Square"""


class Square:
    """Defines the attributes and methods of a square.

    Attributes:
        __size (int): the size of a side of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the attributes of a class Square instance.

        Args:
            size (int): the size of a side of the instantiated object.
            position (tuple): determines no. of trailing spaces on line
        """
        if not isinstance(size, int):
            raise TypeError("size must be an int")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if not isinstance(position, tuple) or len(position) != 2 or \
                not isinstance(position[0], int) or \
                not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(self.__position[0] * " ", end="")
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

    @property
    def position(self):
        """Returns the value of self.__position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the value of self.__position to value"""
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
