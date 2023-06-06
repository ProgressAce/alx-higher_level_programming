#!/usr/bin/python3

"""Module that adds two integers."""


def add_integer(a, b=98):
    """Returns the sum of two integers.

    The arguments are first casted to integers if they are floats.

    Args:
        a(int): first integer.
        b(int): second integer.

    Raises:
        TypeError: if a or b is not of type int.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)
