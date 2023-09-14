#!/usr/bin/python3
""" This module contains the definition of the class MyInt """


class MyInt(int):
    """ Defines the attributes and methods of a MyInt instance.
    Class MyInt is a subclass of class int
    """
    def __eq__(self, other):
        """Sets the use of the '==' symbol
        Attributes:
            other (int): the other value to be compared with self
        Return: Boolean
        """
        return int(self) != other

    def __ne__(self, other):
        """Sets the use of the '!=' symbol
        Atttributes:
            other (int): the other value to be compared with self
        Return: Boolean
        """
        return int(self) == other
