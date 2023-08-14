#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list"""
    new_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return new_list
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list
