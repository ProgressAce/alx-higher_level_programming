#!/usr/bin/python3
"""
A module that returns whether an object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj(object): the object to check.
        a_class(class): the class to check if @object is an instance of it.
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
