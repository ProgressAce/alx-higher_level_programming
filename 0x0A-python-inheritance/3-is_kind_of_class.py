#!/usr/bin/python3

"""Module that checks if an object is an instance, directly or
indirectly, of the specified class."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance of the specified class.

    The instance can be belong to a class that is derived from the
    specified class.

    Arg:
        obj: the object to check.
        a_class: the specified class.

    Return:
        True, if the object is an instance of a class that is has the
        specified class as its base class, directly or indirectly,
        otherwise return False.
    """

    return isinstance(obj, a_class)
