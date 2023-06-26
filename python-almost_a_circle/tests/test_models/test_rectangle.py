#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def testRectangle_valid_arguments(self):
        """
        Test creating an instance of Rectangle with valid arguments.
        """
        r = Rectangle(5, 10, 1, 2)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def testRectangle_invalid_width(self):
        """
        Test creating an instance of Rectangle with invalid width argument.
        """
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 1, 2)

    def testRectangle_invalid_height(self):
        """
        Test creating an instance of Rectangle with invalid height argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 1, 2)

    def testRectangle_invalid_x(self):
        """
        Test creating an instance of Rectangle with invalid x argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 2)

    def testRectangle_invalid_y(self):
        """
        Test creating an instance of Rectangle with invalid y argument.
        """
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 1, "invalid")

    def testRectangle_zero_width(self):
        """
        Test creating an instance of Rectangle with zero width argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 10, 1, 2)

    def testRectangle_zero_height(self):
        """
        Test creating an instance of Rectangle with zero height argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 0, 1, 2)

    def testRectangle_negative_x(self):
        """
        Test creating an instance of Rectangle with negative x argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -1, 2)

    def testRectangle_negative_y(self):
        """
        Test creating an instance of Rectangle with negative y argument.
        """
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 1, -2)


if __name__ == '__main__':
    unittest.main()
