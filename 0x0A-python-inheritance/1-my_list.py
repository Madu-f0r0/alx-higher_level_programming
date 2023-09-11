#!/usr/bin/python3
""" This module contains a derived class MyList which inherits

from the base class list
"""


class MyList(list):
    """ Defines the methods and attributes of objects of class MyList.

    This class inherits the methods and attributes of base class list.
    """

    def print_sorted(self):
        """Prints a list in ascending sort"""

        new_list = sorted(self.copy())
        print(new_list)
