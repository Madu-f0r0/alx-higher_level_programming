#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    for item in sorted(a_dictionary):
        print(item + ":", a_dictionary[item])
