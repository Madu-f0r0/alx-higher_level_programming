#!/usr/bin/python3
""" Module contains the definition of the class BaseGeometry """


class BaseGeometry:
    """ Defines geometrical methods and attributes of instances

    of the class
    """
    def area(self):
        """ Raises a custom exception """
        raise Exception("area() is not implemented")
