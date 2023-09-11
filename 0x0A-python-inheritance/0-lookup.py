#!/usr/bin/python3
""" Module contains the function lookup """


def lookup(obj):
    """ Returns a list of available attributes and methods

    in an object
    """
    return dir(obj)
