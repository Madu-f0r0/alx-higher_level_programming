#!/usr/bin/python3
""" This module contains the function to_json_string which

converts a python object (string) to a JSON string
"""

import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object(string)"""
    return json.dumps(my_obj)
