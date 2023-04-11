#!/usr/bin/python3
"""
A module that defines the function inherit_from.
"""


def inherits_from(obj, a_class):
    """Checks if 

    Args:
        obj(object): the object to check.
        a_class(class): the class to check if @object belongs to a class
        which inherits from it.
    """

    if issubclass(obj.__class__, a_class):
        return True
    else:
        return False
