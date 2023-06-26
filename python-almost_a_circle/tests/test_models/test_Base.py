#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def testBase_default(self):
        """
        Test the default behavior of creating an instance of Base without providing an ID.
        """
        b = Base()
        self.assertEqual(b.id, 1)
        
    def testBase_default1(self):
        """
        Test creating an instance of Base with None as the ID argument.
        """
        b = Base(None)
        self.assertEqual(b.id, 1)


if __name__ == '__main__':
    unittest.main()
