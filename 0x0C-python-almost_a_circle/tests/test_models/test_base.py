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

        b1 = Base()  # with zero args
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)  # with one arg
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

        self.assertRaises(TypeError, Base, 3, 2)

    def test_public_id_attribute(self):
        """Setting the id attribute."""

        b1 = Base()
        b1.id = 5
        self.assertEqual(b1.id, 5)

#    def test_access_private_atrribute(self):
        """All members of a class are not truly private in python.

        Private attributes can still be accessed outside the class.
        """

#        b0 = Base()
#        b0._Base__nb_objects = 1  # Changing the class private attr
#        b0.__nb_objects = 1  # creating a new attribute

if __name__ == '__main__':
    unittest.main()
