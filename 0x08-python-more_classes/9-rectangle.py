#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines the attributes of a class Rectangle.

    Attributes:
        number_of_instances (int): a class attribute representing
        the number of instances of class Rectangle created
        print_symbol (any type): the symbol for string representation
        __width (int): the width of the rectangle
        __height (int): the height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle bases on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """Sets width and height of Rectangle instance to size"""
        return cls(size, size)

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
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes a class Rectangle object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def __str__(self):
        """Returns a string representing the rectangle object

        with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            ret_str = ""
            for i in range(self.__height):
                ret_str += (self.__width * str(self.print_symbol))
                if i != self.__height - 1:
                    ret_str += "\n"
            return ret_str

    def __repr__(self):
        """Returns a string representation of the rectangle object"""
        return "Rectangle" + str((self.__width, self.__height))
