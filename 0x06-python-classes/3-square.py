#!/usr/bin/python3
""" Defines the class Square """


class Square:
    """Defines the attributes of a square.

    Attributes:
        __size (int): the size of a side of a square class
    """

    def __init__(self, size=0):
        """Initializes a square class.

        Args:
            size (int): the size of the square instance
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Computes the area of the square class.

        Returns:
            The area computed
        """
        return self.__size ** 2
