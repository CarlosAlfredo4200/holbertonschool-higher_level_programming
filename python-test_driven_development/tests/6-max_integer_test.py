#!/usr/bin/python3
"""Unittest function max_integer()
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Test a function max_integer()
    """

    def test_len(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)

    def test_string(self):
        list = [1,'hello']
        with self.assertRaises(TypeError):
            max_integer(list)
            
    def test_empty_list(self):
        """Checks the case of an empty list
        """
        list = []
        self.assertEqual(max_integer(list), None)
        
    def test_void_arg(self):
        self.assertEqual(max_integer(), None)
    
if __name__ == '__main__':
    unittest.main()