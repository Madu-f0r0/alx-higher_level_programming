""" Unit test for class Rectangle """

import unittest
import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    """ Tests the functionality of class Rectangle """

    def test_normal_Rectangle(self):
        """Proper object instantiation with integer width and

        height args > 0
        """
        rect = Rectangle(5, 10)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_unique_id(self):
        """Proper object instantiation with integer width and

        height args > 0, and unique id
        """
        rect1 = Rectangle(4, 8)
        rect2 = Rectangle(5, 10, id=12)
        rect3 = Rectangle(6, 12)

        self.assertEqual(rect1.id, 2)
        self.assertEqual(rect2.id, 12)
        self.assertEqual(rect3.id, 3)

    def test_unique_x(self):
        """Object instantiation with int x value >= 0"""
        rect1 = Rectangle(5, 10, x=1)
        rect2 = Rectangle(6, 12, x=15)

        self.assertEqual(rect1.id, 4)
        self.assertEqual(rect2.id, 5)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect2.x, 15)

    def test_unique_y(self):
        """Object instantiation with int y value >= 0"""
        rect1 = Rectangle(5, 10, y=1)
        rect2 = Rectangle(6, 12, y=15)

        self.assertEqual(rect1.id, 6)
        self.assertEqual(rect2.id, 7)
        self.assertEqual(rect1.y, 1)
        self.assertEqual(rect2.y, 15)

    def test_width_setter(self):
        """Sets width of a Rectangle instance to an int > 0"""
        rect1 = Rectangle(5, 10)
        rect1.width = 12
        self.assertEqual(rect1.width, 12)
