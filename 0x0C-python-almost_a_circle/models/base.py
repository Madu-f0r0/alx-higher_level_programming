#!/usr/bin/python3
""" This module contains the definition of the class Base """

import json
import os


class Base:
    """ Manages the id attribute of all other classes in this project.

    Base is the base class of other classes in this project.
    Attributes:
        @__nb_objects (int): Class attribute that is used to initialize the id
        of a Base instance if the @id arg of the instance is not specified
        (None)

        @id (int): Instance attribute representing the id of a Base instance
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the id of a Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of @list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation @json_string"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of @list_objs to a file"""
        json_file = cls.__name__ + ".json"

        if list_objs is None:
            list_objs = []

        with open(json_file, "w", encoding="utf-8") as jsonFile:
            list_dicts_objs = [obj.to_dictionary() for obj in list_objs]
            jsonFile.write(cls.to_json_string(list_dicts_objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance wih all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_obj = cls(1)
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file_name = cls.__name__ + ".json"

        if os.path.exists(file_name):
            with open(file_name, encoding="utf-8") as jsonFile:
                json_list = json.load(jsonFile)

            return [cls.create(**instance_dict) for instance_dict in json_list]
        return []
