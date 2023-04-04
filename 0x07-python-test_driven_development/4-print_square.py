#!/usr/bin/python3

"""
This module defines function print_square(size)
"""


def print_square(size):
    """prints a square using the # character.

    Args:
        size(int): the length of the square.

    Raises:
        TypeError: if size is a non-integer.
        ValueError: if size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    # print square
    if size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print('#', end='')

            print()
