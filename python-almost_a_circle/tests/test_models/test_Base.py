#!/usr/bin/python3

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def testBase_default(self):
        b = Base()
        self.assertEqual(b.id, 1)
        
    def testBase_default1(self):
        b = Base(None)
        self.assertEqual(b.id, 1)


if __name__ == '__main__':
    unittest.main()
