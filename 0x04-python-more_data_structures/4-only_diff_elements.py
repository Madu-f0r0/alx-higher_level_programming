#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all the elements present in only one set"""
    new_set = set(set_1 ^ set_2)
    return new_set
