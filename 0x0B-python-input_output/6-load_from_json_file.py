#!/usr/bin/python3
""" This module contains the function load_from_json_file """

import json


def load_from_json_file(filename):
    """ Creates an object from a JSON file """
    with open(filename, encoding='utf-8') as jsonFile:
        return json.load(jsonFile)
