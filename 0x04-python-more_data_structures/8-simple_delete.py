#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Deletes a key in a dictionary"""
    if a_dictionary.get(key, "absent") != "absent":
        a_dictionary.pop(key)
    return a_dictionary
