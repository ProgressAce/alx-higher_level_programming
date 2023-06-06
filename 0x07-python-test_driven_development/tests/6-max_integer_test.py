#!/usr/bin/python3

"""Unittest for max_integer[..]."""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittests for max_integer."""

    def test_empty_list(self):
        self.assertEqual(None, max_integer([]))

    def test_one_or_more_elements(self):
        self.assertEqual(3, max_integer([1, 3, 2]))
        self.assertEqual(3, max_integer([1, 3, 3]))
        self.assertEqual(1, max_integer([1]))

    def test_string_element(self):
        self.assertEqual('abc', max_integer(['abc', 'ABC']))

    def test_mixed_elements(self):
        self.assertEqual(2.2, max_integer([2.2, 2]))

        self.assertRaises(TypeError, max_integer, ['a', 3, 2])
        self.assertRaises(TypeError, max_integer, [None, 3, 2])
        self.assertRaises(TypeError, max_integer, [1.5j, 3, 2])
        self.assertRaises(TypeError, max_integer, [{}, 3, 2])
        self.assertRaises(TypeError, max_integer, [{3}, 3, 2])

    def test_incorrect_arg(self):
        self.assertEqual('u', max_integer('abacus'))

        with self.assertRaises(TypeError):
            max_integer(None)
            max_integer({'a': 1, 'b': 2})
            max_integer({5, 3, 4})
            max_integer(frozenset('abacus'))
