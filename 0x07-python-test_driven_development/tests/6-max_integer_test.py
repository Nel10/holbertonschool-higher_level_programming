#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_documentation(self):
        self.assertTrue(len(__import__("6-max_integer").__doc__) > 0)
        self.assertTrue(len(max_integer.__doc__) > 0)

    def test_positives(self):
        self.assertEqual(max_integer([2, 4, 5, 9]), 9)
        self.assertEqual(max_integer([7, 6, 1, 4]), 7)
        self.assertEqual(max_integer([2, 4]), 4)
        self.assertEqual(max_integer([0, -5, 6]), 6)
        self.assertEqual(max_integer([200, 489, 120095, 98709876]), 98709876)
        self.assertEqual(max_integer([-200, -478, -590823, -3049]), -200)
        self.assertEqual(max_integer([-89898, -90989, -5, -654765]), -5)

    def test_no_list(self):
      self.assertRaises(TypeError, max_integer, [1, 2, "hi", 3])
      self.assertRaises(TypeError, max_integer, [1, 2, ["Shannel"], 3])

      text_list = [1, 2, False, 3]
      self.assertRaises(TypeError)

      text_list = [7, 78, True, 3]
      self.assertRaises(TypeError)

if __name__ == '__main__':
    unittest.main()
