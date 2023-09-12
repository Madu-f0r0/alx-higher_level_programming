#!/usr/bin/python3
""" This module contains function read_file which reads a text file """


def read_file(filename=""):
    """ Reads a text file and prints it to stddout """
    with open(filename, encoding='utf-8') as openFile:
        print(openFile.read(), end="")
