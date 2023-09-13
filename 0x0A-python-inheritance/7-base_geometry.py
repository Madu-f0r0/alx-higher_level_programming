#!/usr/bin/python3
""" Module contains the definition of the class BaseGeometry """


class BaseGeometry:
    """ Defines geometrical methods and attributes of instances
    of the class BaseGeometry
    """

    def area(self):
        """ Raises a custom exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates @value as an int class or not

        Args:
            @name (string): the name of the object to be
            validated

            @value: the value of the object to be validated
        """
        if type(value) is not int:
            raise TypeError("{} is not an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
