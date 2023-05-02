#!/usr/bin/python3
"""
A module for testing class Base.
"""

from models.base import Base
import unittest

class TestBaseInstantiation(unittest.TestCase):
    """Unittests for testing instantiation of class Base."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_with_arg(self):
        b1 = Base(7)
        b2 = Base(30)
        self.assertEqual(b1.id, 7)
        self.assertEqual(b2.id, 30)

    def test_some_args(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(12)
        b4 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 3)
