#!/usr/bin/python3
""" This module contains the function class_to_json """


def class_to_json(obj):
    """ Returns a dictionary description for JSON seriaization
    of an object
    """
    return obj.__dict__
