#!/usr/bin/python3
""" This module contains a class Rectangle that is derived from

the base class BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle is a subclass of class BaseGeometry

    Attributes:
        @__width (int): the width of a Rectangle instance
        @__height (int): the height of a Rectangle instance
    """

    def __init__(self, width, height):
        """ Initializes the width and height attributes of a

        Rectangle instance
        Args:
            @width: to be passed to the width of the object
            @height: to be passed to the height of the object
        """

        self.integer_validator('width', width)
        self.__width = width

        self.integer_validator('height', height)
        self.__height = height
