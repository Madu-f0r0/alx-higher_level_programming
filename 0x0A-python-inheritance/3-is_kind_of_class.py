#!/usr/bin/python3
""" Module contains the is_kind_of_class function """


def is_kind_of_class(obj, a_class):
    """ Check if an object is an instance of a specified class

    or an instance of a class that inherited from the specified
    class
    """
    return isinstance(obj, a_class)
