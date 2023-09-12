#!/usr/bin/python3
""" This module contains the definition of the class Student """


class Student:
    """ Defines the attributes and methods of a Student instance.
    Attributes:
        @first_name (str): the first name of the student
        @last_name (str): the last name of the student
        @age: the age in years of the student
    """

    def __init__(self, first_name, last_name,  age):
        """ Initializes the first name, last name, and age
        of a Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Returns the dict representation of a Student instance """
        return self.__dict__
