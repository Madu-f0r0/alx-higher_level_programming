#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by another in a list"""

    new_list = list(map((lambda x: replace if x == search else x), my_list))

    return new_list
