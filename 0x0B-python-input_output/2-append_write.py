#!/usr/bin/python3
""" This module contains the append_write function that appends

a string at the end of a text file
"""


def append_write(filename="", text=""):
    """Appends a string at the end of a file.

    Returns: the number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as openFile:
        return openFile.write(text)
