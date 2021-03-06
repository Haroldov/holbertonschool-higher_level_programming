#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """clas for test """
    def test_none(self):
        """ test 1"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_regular_list(self):
        """ test 2"""
        self.assertEqual(max_integer([1, 4, 6, 7]), 7)

    def test_string(self):
        """ test 3"""
        with self.assertRaises(TypeError):
            max_integer(["hello", 90])

    def test_list_string(self):
        """ test 4"""
        with self.assertRaises(TypeError):
            max_integer(["h", "5", 8])

    def test_empty_list(self):
        """ test 5"""
        self.assertEqual(max_integer([]), None)

    def test_max_beginning(self):
        """ test 6"""
        self.assertEqual(max_integer([15, 9, 8]), 15)

    def test_max_middle(self):
        """ test 7"""
        self.assertEqual(max_integer([6, 9, 8]), 9)

    def test_neg_num(self):
        """ test 7"""
        self.assertEqual(max_integer([6, 9, -8]), 9)

    def test_allneg_num(self):
        """ test 7"""
        self.assertEqual(max_integer([-6, -9, -8]), -6)

    def test_one_elem(self):
        """ test 7"""
        self.assertEqual(max_integer([-6]), -6)
