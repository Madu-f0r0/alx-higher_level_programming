"""Unit test for class Base"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClassID(unittest.TestCase):
    """Tests the funtionality of class Base id assignment"""

    def test_id_none(self):
        """Tests for when @id is not initialized"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_positive_id(self):
        """Tests for when id is initialized with a postive int"""
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_zero_id(self):
        """Tests for when id is initialized to 0"""
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_negative_id(self):
        """Tests for when id is initialized with a negative int"""
        b = Base(-15)
        self.assertEqual(b.id, -15)


class TestBaseClassToJSONString(unittest.TestCase):
    """Tests the functionality of class Base method to_json_string()"""

    def test_rectangle_1_list_dictionaries(self):
        """Tests to_json_string() with a list of dictionaries 
        on a Rectangle instance
        """
        rect = Rectangle(10, 7, 2, 8, 12)
        dictionary = rect.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result_string =  '[{"id": 12, "width": 10, "height": 7, "x": 2, "y": 8}]'

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, result_string)

    def test_square_1_list_dictionaries(self):
        """Tests to_json_string() with a list of dictionaries
        on a Square instance
        """
        sq = Square(10, 2, 8, 12)
        dictionary = sq.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        result_string =  '[{"id": 12, "size": 10, "x": 2, "y": 8}]'

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, result_string)

    def test_2_list_dictionaries(self):
        """Tests a list with two dictionaries"""
        dict_list = [{'id': 13, 'x': 2}]
        dict_list.append({'id': 14, 'x': 3})
        json_dictionary = Base.to_json_string(dict_list)

        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, \
            '[{"id": 13, "x": 2}, {"id": 14, "x": 3}]')

    def test_None_list_dictionaries(self):
        """Tests to_json_string() when list_dictionaries is None"""
        json_dictionary = Base.to_json_string(None)
        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, "[]")

    def test_empty_list_dictionaries(self):
        """Tests to_json_string() when list_dictionaries = []"""
        json_dictionary = Base.to_json_string([])
        self.assertTrue(type(json_dictionary), "<class 'str'>")
        self.assertEqual(json_dictionary, "[]")
