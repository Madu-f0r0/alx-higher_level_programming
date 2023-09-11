#!/usr/bin/python3
""" Module contains the inherits_from function """


def inherits_from(obj, a_class):
    """Checks if the object @obj is an instance of a class that

    inherited (directly or indirectly) from the class @a_class
    """
    if a_class is not type(obj):
        return issubclass(type(obj), a_class)
