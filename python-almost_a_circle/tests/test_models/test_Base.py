#!/usr/bin/python3

import unittest
from models.base import Base
class TestBase(unittest.TestCase):
    
    
    def testBase_default(self):
        self.assertEqual(Base(None))
        
        
if __name__ == '__main__':
    unittest.main()