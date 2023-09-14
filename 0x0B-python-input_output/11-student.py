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

    def to_json(self, attrs=None):
        """ Returns the dict representation of a Student instance """
        if type(attrs) is list:
            new_dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    new_dict[attr] = self.__dict__.get(attr)
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of a Student instance """
        for key in json.keys():
            self.__dict__[key] = json.get(key)
