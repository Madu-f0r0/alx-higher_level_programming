#!/usr/bin/python3
"""This module contains the definition of the class Rectangle.

class Rectangle is a sublcass of class Base.
"""

from models.base import Base

class Rectangle(Base):
    """Defines the attributes and methods of the Rectangle class.
    
    Attributes:
        @width: the width of the Rectangle instance
        @height: the height of the rectangle instance
        @x:
        @y:
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance with its attributes"""
        super().__init__(id)

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif y < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    @property
    def width(self):
        """Returns the value of self.width to the user"""
        return self.__width

    @width.setter
    def width(self, value):
        """Allows user set the value of self.width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Returns the value of self.height to the user"""
        return self.__height

    @height.setter
    def height(self, value):
        """Allows user set the value of self.height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Returns the value of self.x to the user"""
        return self.__x

    @x.setter
    def x(self, value):
        """Allows user set the value of self.x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value


    @property
    def y(self):
        """Returns the value of self.y to the user"""
        return self.__y

    @y.setter
    def y(self, value):
        """Allows user set the value of self.y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
