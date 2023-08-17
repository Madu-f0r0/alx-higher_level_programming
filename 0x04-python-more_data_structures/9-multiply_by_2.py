#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values mutliplied by 2"""
    new_dict = {x: a_dictionary[x] * 2 for x in a_dictionary}
    return new_dict
