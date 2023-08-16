#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds the unique elements in a list"""
    list_sum = 0

    for x in set(my_list):
        list_sum += x

    return list_sum
