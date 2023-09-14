#!/usr/bin/python3
""" This module contains the function add_attribute """


def add_attribute(obj, att_name, value):
    """ Adds a new attribute to an object.
    Args:
        @obj: the object to which an attribute is to be added
        @att_name (str): the name of the new attribute
        @value: the value of the new attribute
    """
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, att_name, value)
