#!/usr/bin/python3
"""
A module that defines the function is_same_class.
"""


def is_same_class(obj, a_class):
    """Checks if @obj is exactly an instance
    of the specified class, otherwise False.

    Args:
        obj(object): the object to check.
        a_class(class): the class to check if @object belongs to it
    """

    if type(obj) == a_class:
        return True
    else:
        return False
