#!/usr/bin/python3
""" Contains the function write_file that a string to a text file """


def write_file(filename="", text=""):
    """Writes a string to a text file. Returns the

    number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as openFile:
        return openFile.write(text)
