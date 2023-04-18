#!/usr/bin/python3
"""
A module that defines a function is_kind_of_class.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or one its subclasses.

    Args:
        obj(object): the object to check.
        a_class(class): the class to check if @object is an instance of it.

    Returns:
        True if the checked object is an instance of the specified class
        or one of its subclassed, otherwise False.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
