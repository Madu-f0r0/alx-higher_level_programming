#!/usr/bin/python3
""" This module contains the function from_json_string.

This function converts a JSON string to a python object
"""

import json


def from_json_string(my_str):
    """ Returns an object represented by a JSON string """
    return json.loads(my_str)
