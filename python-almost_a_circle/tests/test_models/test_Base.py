#!/usr/bin/python3

import unittest
from models.base import Base
b = Base()
b1 = Base()
class TestBase(unittest.TestCase):
    
    
    def testBase_default(self, b):
        self.assertEqual(b.id, 1)
        
    def testBase_default(self, b):
        self.assertEqual(b1.id(None), 1)
        
     
         
     
        
        
if __name__ == '__main__':
    unittest.main()