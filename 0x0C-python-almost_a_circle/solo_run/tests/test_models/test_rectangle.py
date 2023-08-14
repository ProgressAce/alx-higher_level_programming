#!/usr/bin/python3
"""Unittesting for the Rectangle class."""
import unittest
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Unit tests for instantiation evaluation of the Rectangle class."""

    def test_base_inheritance(self):
        """Test the inheritance of the Rectangle's parent class."""

        r1 = Rectangle(1, 4)
        r2 = Rectangle(3, 5)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2._Base__nb_objects, 2)

    def test_zero_or_one_arg(self):
        """Case when zero or one argument is received."""

        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, 3)

    def test_two_args(self):
        """Case when two arguments are received."""

        r3 = Rectangle(2, 4)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 4)

    def test_three_and_four_args(self):
        """The optional third and fourth arguments are for x and y axis."""

        r4 = Rectangle(2, 4, 1)
        self.assertEqual(r4.x, 1)
        r5 = Rectangle(2, 4, 1, 3)
        self.assertEqual(r5.y, 3)
        r6 = Rectangle(2, 4, 1, 3, 7)
        self.assertEqual(r6.id, 7)

    def test_x_y_and_id_defaults_args(self):
        """Testting that the default values for x,y and id are correct.

        If no id is given as the 5th argument, then the number of objects
        created will be set as the id of the object, all according to the
        Base class implementation. If an id is given then the number of
        objects is not increased for that objects creation."""

        r7 = Rectangle(3, 2)
        self.assertEqual(r7.x, 0)
        self.assertEqual(r7.y, 0)
        self.assertEqual(r7.id, 6)

    def test_six_or_more_args(self):
        """There should be no more than 5 arguments."""

        self.assertRaises(TypeError, Rectangle, 2, 4, 1, 1, 3, 6)

#    def test_access_private_instance_attributes(self):
        """Making sure that the private instance attributes cannot """

        #r1 = Rectangle(2, 4)
        #self.assertEqual(r1.width, 2)
        #self.assertEqual(r1.length, 4)

class TestRectangleWidth(unittest.TestCase):
    """Unit tests for validating the width argument."""

    def test_integer(self):
        """Accepts integer argument."""

        r1 = Rectangle(4, 2)
        self.assertEqual(r1.width, 4)

    def test_negative_or_zero_int(self):
        """Negative and zero integers are not accepted."""

        with self.assertRaises(ValueError):
            r1 = Rectangle(-2, 1)
            r2 = Rectangle(0, 1)

    def test_string(self):
        """A string is not accepted."""

        self.assertRaises(TypeError, Rectangle, 'six', 4)

    def test_float(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 3.1, 4)

    def test_complex_num(self):
        """A complex number is not accepted."""

        self.assertRaises(TypeError, Rectangle, 2j, 4)

    def test_list(self):
        """A list is not accepted."""

        self.assertRaises(TypeError, Rectangle, [1, 2], 4)

    def test_tuple(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, (2, 3), 4)

    def test_range(self):
        """A range is not accepted."""

        self.assertRaises(TypeError, Rectangle, range(1), 4)

    def test_boolean(self):
        """A boolean is accepted as 0 or 1."""

        self.assertEqual(Rectangle(True, 4).width, 1)

    def test_bytes(self):
        """A byte is not accepted."""

        self.assertRaises(TypeError, Rectangle, b'5', 4)

    def test_bytearray(self):
        """A bytearray is not accepted."""

        self.assertRaises(TypeError, Rectangle, bytearray(5), 4)

    def test_memoryview(self):
        """A memoryview is not accepted."""

        self.assertRaises(TypeError, Rectangle, memoryview(bytes(3)), 4)

    def test_NoneType(self):
        """A NoneType is not accepted."""

        self.assertRaises(TypeError, Rectangle, None, 4)

class TestRectangleHeight(unittest.TestCase):
    """Unit tests for validating the height argument."""

    def test_integer(self):
        """Accepts integer argument."""

        r1 = Rectangle(4, 2)
        self.assertEqual(r1.height, 2)

    def test_negative_or_zero_int(self):
        """Negative and zero integers are not accepted."""

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, -1)
            r2 = Rectangle(2, 0)

    def test_string(self):
        """A string is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, 'six')

    def test_float(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, 3.1)

    def test_complex_num(self):
        """A complex number is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, 2j)

    def test_list(self):
        """A list is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, [1, 2])

    def test_tuple(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, (2, 3))

    def test_range(self):
        """A range is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, range(1))

    def test_boolean(self):
        """A boolean is accepted as 0 or 1."""

        self.assertEqual(Rectangle(4, True).height, 1)

    def test_bytes(self):
        """A byte is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, b'5')

    def test_bytearray(self):
        """A bytearray is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, bytearray(5))

    def test_memoryview(self):
        """A memoryview is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, memoryview(bytes(3)))

    def test_NoneType(self):
        """A NoneType is not accepted."""

        self.assertRaises(TypeError, Rectangle, 4, None)

class TestRectangleX(unittest.TestCase):
    """Unit tests for validating the x argument."""

    def test_integer(self):
        """Accepts integer argument."""

        r1 = Rectangle(4, 2, 1)
        self.assertEqual(r1.x, 1)

    def test_negative_or_zero_int(self):
        """Negative and zero integers are not accepted."""

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 1, -2)
            r2 = Rectangle(2, 1, 0)

    def test_string(self):
        """A string is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, '2')

    def test_float(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 2.5)

    def test_complex_num(self):
        """A complex number is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 2j)

    def test_list(self):
        """A list is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, [1, 2])

    def test_tuple(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, (2, 3))

    def test_range(self):
        """A range is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, range(1))

    def test_boolean(self):
        """A boolean is accepted as 0 or 1."""

        self.assertEqual(Rectangle(6, 4, True).x, 1)

    def test_bytes(self):
        """A byte is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, b'5')

    def test_bytearray(self):
        """A bytearray is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, bytearray(5))

    def test_memoryview(self):
        """A memoryview is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, memoryview(bytes(3)))

    def test_NoneType(self):
        """A NoneType is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, None)

class TestRectangleY(unittest.TestCase):
    """Unit tests for validating the y argument."""

    def test_integer(self):
        """Accepts integer argument."""

        r1 = Rectangle(4, 2, 1, 2)
        self.assertEqual(r1.y, 2)

    def test_negative_or_zero_int(self):
        """Negative and zero integers are not accepted."""

        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 1, 1, -2)
            r2 = Rectangle(2, 1, 1, 0)

    def test_string(self):
        """A string is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, '2')

    def test_float(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, 2.3)

    def test_complex_num(self):
        """A complex number is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, 3j)

    def test_list(self):
        """A list is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, [1, 2])

    def test_tuple(self):
        """A float is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, (2, 3))

    def test_range(self):
        """A range is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, range(1))

    def test_boolean(self):
        """A boolean is accepted as 0 or 1."""

        self.assertEqual(Rectangle(6, 4, 1, True).y, 1)

    def test_bytes(self):
        """A byte is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, b'5')

    def test_bytearray(self):
        """A bytearray is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, bytearray(5))

    def test_memoryview(self):
        """A memoryview is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, memoryview(bytes(3)))

    def test_NoneType(self):
        """A NoneType is not accepted."""

        self.assertRaises(TypeError, Rectangle, 6, 4, 1, None)

class TestRectangleSpecialAndAdditionalMethods(unittest.TestCase):
    """Unit tests for the additional and special methods."""

    def test_area(self):
        """Tests that area() returns the correct output."""

        self.assertRaises(ValueError, Rectangle, -1, 5)
        r1 = Rectangle(3, 5)
        self.assertEqual(r1.area(), 15)
        r2 = Rectangle(6, 9, 2, 3, 12)
        self.assertEual(r2.area(), 54)

    def test_display(self):
        """Test the correct outputs for the display() method."""

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.display(), '###\n###\n')
        r2 = Rectangle(2, 4)
        self.assertEqual(r2.display(), '##\n##\n##\n##\n')

        r3 = Rectangle(2, 3, 2, 2)
        self.assertEqual(r3.display(), '\n\n  ##\n  ##\n  ##\n')
        r4 = Rectangle(3, 2, 1, 0)
        self.assertEqual(r4.display(), ' ###\n ###\n')

    def test_str_special_method(self):
        """Test the correct output for the special __str__() method."""

        r1 = Rectangle(3, 6)
        self.assertEqual(print(r1), '[Rectangle] (1) 0/0 - 3/6')
        r1 = Rectangle(2, 4, 1, 3, 8)
        self.assertEqual(print(r1), '[Rectangle] (2) 3/8 - 2/4')

    def test_update(self):
        """Test that update() updates the correct argument."""

        r1 = Rectangle(8, 8, 8, 8)
        self.assertEqual(print(r1), '[Rectangle] (3) 8/8 - 8/8')

        r1.update(21)
        self.assertEqual(print(r1), '[Rectangle] (4) 3/8 - 21/4')

        r1.update(21, 22)
        self.assertEqual(print(r1), '[Rectangle] (5) 3/8 - 21/22')

        r1.update(21, 22, 23)
        self.assertEqual(print(r1), '[Rectangle] (6) 23/8 - 21/22')

        r1.update(21, 22, 23, 24)
        self.assertEqual(print(r1), '[Rectangle] (7) 23/24 - 21/22')
