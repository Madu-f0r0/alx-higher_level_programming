#!/usr/bin/python3
"""Contains the definition of class Square"""


class Square:
    """Defines the attributes of a square.

    Args:
        size(int): the size of the object square

    Raises:
        TypeError: raised if size is not an integer
        ValueError: raised if size is less than 0

    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
