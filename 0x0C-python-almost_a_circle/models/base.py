#!/usr/bin/python3
""" This module contains the definition of the class Base """


class Base:
    """ Manages the id attribute of all other classes in this project.

    Base is the base class of other classes in this project.
    Attributes:
        @__nb_objects (int): Class attribute that is used to initialize the id of
        a Base instance if the @id arg of the instance is not specified (None)

        @id (int): Instance attribute representing the id of a Base instance 
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the id of a Base instance """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
