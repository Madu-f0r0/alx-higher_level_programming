""" Unit test for class Base"""

import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """ Tests the funtionality of class Base """

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
