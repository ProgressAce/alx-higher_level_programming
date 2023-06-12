#!/usr/bin/python3

"""Module that checks if an object is an exact instance of the specified class.
"""


def is_same_class(obj, a_class):
    """Check if an object belongs directly to the specified class.

    Args:
        obj: the object to check.
        a_class: the specified class.

    Return:
        True if the object is an exact instance of the specified class,
        otherwise returns False.
    """

    return type(obj) == a_class
