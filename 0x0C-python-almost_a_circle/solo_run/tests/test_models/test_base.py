#!/usr/bin/python3
"""Unittesting the Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittesting the base.py file for different test cases."""

    def test_initialisation(self):
        """Testing initialisation of the base instance.

        @id is assumed to be an int and is therefore not tested.
        """

        b2 = Base()  # with zero args
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base(12)  # with one arg
        self.assertEqual(b4.id, 12)
        b5 = Base()
        self.assertEqual(b5.id, 4)

    def test_parameter_number(self):
        """Test how many parameters the class handles.

        The class only accepts zero or one argument."""

        b5 = Base()  # zero arguments
        self.assertEqual(b5, b5)
        b6 = Base(3)  # optional argument
        self.assertEqual(b6, b6)
        self.assertRaises(TypeError, Base, 3, 2)  # more than 1 arg

    def test_public_id_attribute(self):
        """Test that the id attribute is public."""

        b7 = Base()
        b7.id = 19
        self.assertEqual(b7.id, 19)

    def test_access_private_atrribute(self):
        """Test that Base's private class attribute cannot be accessed.

        Private attributes can still be accessed outside the class
        in python.
        """

        b1 = Base()
        self.assertRaises(AttributeError, b1.__nb_objects)
        b1._Base__nb_objects = 1  # Changing the class private attr
        self.assertEqual(b1._Base__nb_objects, 1)  # creating a new attribute

if __name__ == '__main__':
    unittest.main()
