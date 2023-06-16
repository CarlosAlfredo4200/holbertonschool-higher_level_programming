#!/usr/bin/python3
"""Unittest function max_integer()
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_len(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(max_integer(arr), 4)

    def test_string(self):
        list = [1,'hello']
        with self.assertRaises(TypeError):
            max_integer(list)
            
    def test_empty_list(self):
        """Checks the case of an empty list
        """
        _list = []
        self.assertEqual(max_integer(_list), None)
    
if __name__ == '__main__':
    unittest.main()