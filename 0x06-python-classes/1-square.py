#!/usr/bin/python3
"""Class Square defines the attributes of a square"""


class Square:
    """ Defines the properties of a square.

    To be specific, the square in question is the shape which has
    all sides of equal length.

    Args:
        size (int): the length/width of the square

    """

    def __init__(self, size):
        self.__size = size
