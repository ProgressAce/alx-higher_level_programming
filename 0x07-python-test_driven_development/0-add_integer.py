#!/usr/bin/python3

"""This module defines function add_integer(a, b=98)"""


def add_integer(a, b=98):
    """Returns the addition of a and b.

    a and b are casted to int if they are floats.

    Args:
        a(int): the first number.
        b(int): the second number.

    Raises:
        TypeError: if a or b are not of type integer or float.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
