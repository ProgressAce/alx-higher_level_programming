#!/usr/bin/python3
"""
A unittest module for testing the Rectangle class.
"""


from models.rectangle import Rectangle
from models.base import Base
import unittest

class TestRectangleInstantiation(unittest.TestCase):
    """Unittest for testing the instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        assertIsInstance(Rectangle(6, 4), Base())

    def test_no_args(self):
        with assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with assertRaises(TypeError):
            Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(8, 2)
        r2 = Rectangle(2, 8)
        assertEqual(r1.id, 1)
        assertEqual(r2.id, 2)

    def test_three_args(self):
        r1 = Rectangle(4, 2, 1)
        assertEqual(r1.x, 1)

    def test_four_args(self):
        r1 = Rectangle(4, 2, 1, 1)
        assertEqual(r1.y, 1)

    def test_five_args(self):
        r1 = Rectangle(5, 2)
        r2 = Rectangle(3, 6)
        r3 = Rectangle(4, 2, 1, 1, 5)
        assertEqual(r1.id, 1)
        assertEqual(r2.id, 2)
        assertEqual(r3.id, 5)

    def test_more_than_five_args(self):
        with assertRaises(TypeError):
            Rectangle(8, 3, 1, 0, 12, 6)

    def test_width_privacy(self):
        with assertRaises(AttributeError):
            print(Rectangle(6, 3, 1, 1, 2).__width)

    def test_height_privacy(self):
        with assertRaises(AttributeError):
            print(Rectangle(6, 3, 1, 1, 2).__height)

    def test_x_privacy(self):
        with assertRaises(AttributeError):
            print(Rectangle(6, 3, 1, 1, 2).__x)

    def test_y_privacy(self):
        with assertRaises(AttributeError):
            print(Rectangle(6, 3, 1, 1, 2).__y)

    def test_width_getter(self):
        r = Rectangle(4, 3)
        assertEqual(r.width, 4)

    def test_width_setter(self):
        r = Rectangle(5, 2)
        r.width = 3
        assertEqual(r.width, 3)

    def test_height_getter(self):
        r = Rectangle(4, 3)
        assertEqual(r.height, 3)

    def test_height_setter(self):
        r = Rectangle(5, 2)
        r.height = 6
        assertEqual(r.height, 6)

    def test_x_getter(self):
        r = Rectangle(4, 3, 1)
        assertEqual(r.x, 1)

    def test_x_setter(self):
        r = Rectangle(5, 2, 1)
        r.x = 2
        assertEqual(r.x, 2)

    def test_y_getter(self):
        r = Rectangle(4, 3, 1, 3)
        assertEqual(r.y, 3)

    def test_y_setter(self):
        r = Rectangle(5, 2, 1, 3)
        r.y = 2
        assertEqual(r.y, 2)

class TestRectangleWidth(unittest.TestCase):

    def test_int_arg(self):
        assertEqual(Rectangle(5, 2).width, 5)

    def test_none_arg(self):
        with self.ssertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(None, 3)

    def test_float_arg(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(3.1, 3)

    def test_complex_num_arg(self):
        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(4j, 3)

    def test_str_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle("abacus", 3)

    def test_bool_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(True, 3)

    def test_infinity_num_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(float('inf'), 3)

    def test_nan_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(float('nan'), 3)

    def test_list_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle([4, 8, 5], 3)

    def test_tuple_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle((3, 8, 4), 3)

    def test_range_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(range(3), 3)

    def test_dict_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle({'name': 'Wonder Boy', 'age': 19}, 3)

    def test_set_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle({2, 8, 3, 3}, 3)

    def test_frozenset_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(frozenset({1, 8, 1, 1}), 3)

    def test_bytes_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(b'Geek', 3)

    def test_bytearray_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(bytearray(3), 3)

    def test_memoryview_arg(self):
        with assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(memoryview(bytes(3)), 3)

class TestRectangleHeight(unittest.TestCase):
    def test_int_arg(self):
        assertEqual(Rectangle(7, 4).height, 4)

    def test_none_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, None)

    def test_float_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, 5.5)

    def test_complex_num_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, 2j)

    def test_str_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, 'Seven')

    def test_bool_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, True)

    def test_infinity_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, float('inf'))

    def test_nan_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, float('nan'))

    def test_list_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, [])

    def test_tuple_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, tuple())

    def test_set_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, set())

    def test_frozenset_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, frozenset())

    def test_byte_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, b'Seven')

    def test_bytearray_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, bytearray(4))

    def test_memoryview_arg(self):
        with assertRaisesRegex(TypeError, 'height must be an integer'):
            Rectangle(7, memoryview(bytes(3)))

class TestRectangleX(unittest.TestCase):

    def test_int_arg(self):
        assertEqual(Rectangle(5, 2, 1).x, 1)

    def test_none_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 2, None)

    def test_float_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, 2.1)

    def test_complex_num_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, 2j)

    def test_str_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, '1')

    def test_bool_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(44, 3, True)

    def test_infinity_num_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, float('inf'))

    def test_nan_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, float('nan'))

    def test_list_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, [4, 8, 5])

    def test_tuple_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, (3, 8, 4))

    def test_range_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, range(3))

    def test_dict_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, {'x': 1})

    def test_set_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, {1, 2, 2})

    def test_frozenset_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, frozenset({1, 1}))

    def test_bytes_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, b'Geek')

    def test_bytearray_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, bytearray(3))

    def test_memoryview_arg(self):
        with assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, memoryview(bytes(3)))

class TestRectangleY(unittest.TestCase):

    def test_int_arg(self):
        assertEqual(Rectangle(5, 2, 1, 2).y, 2)

    def test_none_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 2, 1, None)

    def test_float_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, 2.1)

    def test_complex_num_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, 2j)

    def test_str_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, '1')

    def test_bool_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, True)

    def test_infinity_num_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, float('inf'))

    def test_nan_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, float('nan'))

    def test_list_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, [4, 8, 5])

    def test_tuple_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, (3, 8, 4))

    def test_range_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, range(3))

    def test_dict_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, {'y': 1})

    def test_set_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, {2, 2})

    def test_frozenset_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, frozenset({1, 1}))

    def test_bytes_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, b'two')

    def test_bytearray_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, bytearray(3))

    def test_memoryview_arg(self):
        with assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 1, memoryview(bytes(3)))

class TestRectangleMethods(unittest.TestCase):
    """Unittest for testing the methods of a Rectangle instance."""

    def test_area(self):
        r1 = Rectangle(3, 2)
        assertEqual(print(r1.area()), 6)

        r2 = Rectangle(2, 10)
        assertEqual(print(r2.area()), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        assertEqual(print(r3.area()), 56)
