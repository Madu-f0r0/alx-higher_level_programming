#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines the attributes of a class Rectangle.

    Attributes:
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes the fields of each class Rectangle object.

        args:
            width (int): the width of the instantiated object
            height (int): the height of the instantiated object
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """Returns the value of self.__width to the user"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of self.__width to value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of self.__height to the user"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of self.__height to value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Computes and returns the area of a rectangle object"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes and returns the perimeter of a rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
