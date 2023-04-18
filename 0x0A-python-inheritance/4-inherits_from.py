#!/usr/bin/python3
"""
A module that defines the function inherit_from.
"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherits from the
    specified class.

    Args:
        obj(object): the object to check.
        a_class(class): the class to check if the object belongs to a class
            that inherits from it.
    """

    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
