#!/usr/bin/python3
""" Module contains is_same_class function """


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of the

    specified class.
    Returns: True or False
    """
    if type(obj) is a_class:
        return True
    else:
        return False
