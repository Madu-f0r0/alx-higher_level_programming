#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if a_dictionary is None:
        return None
    for i in list(a_dictionary):
        if a_dictionary[i] == sorted(a_dictionary.values())[-1]:
            return i
