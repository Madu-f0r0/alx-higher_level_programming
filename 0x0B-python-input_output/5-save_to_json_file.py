#!/usr/bin/python3
""" This module contains the function save_to_json_file. """

import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file via JSON representation"""
    with open(filename, 'w', encoding='utf-8') as jsonFile:
        json.dump(my_obj, jsonFile)
