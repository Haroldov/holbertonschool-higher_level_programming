#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 4, 6, 7]), 7)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer("hello")

    def test_list_string(self):
        with self.assertRaises(TypeError):
            max_integer(["h", "5", 8])

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)
