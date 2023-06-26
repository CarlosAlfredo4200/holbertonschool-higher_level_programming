#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def testRectangle_default(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r3.width, 10)


    def testRectangle_infinity_arguments(self):
        """
        Test creating an instance of Rectangle with infinity as arguments.
        """
        with self.assertRaises(ValueError):
            Rectangle(float('inf'), float('inf'), float('inf'), float('inf'))

    def testRectangle_none_arguments(self):
        """
        Test creating an instance of Rectangle with None as arguments.
        """
        with self.assertRaises(ValueError):
            Rectangle(None, None, None, None)


if __name__ == '__main__':
    unittest.main()
