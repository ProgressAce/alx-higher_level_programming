#!/usr/bin/python3

"""Checks if an object's class is a subclass of the specified class."""


def inherits_from(obj, a_class):
    """Checks if an object's class inherits from the specified class.

    The object's class should not be the same as @a_class since that
    would mean that @obj's class is not a subclass of @a_class and will
    result in False being returned.

    Arg:
        obj: the object whose class will be checked.
        a_class: the specified class.

    Return:
        True, if the object's class is a subclass of the specified class,
        otherwise return False.
    """

    return (issubclass(obj.__class__, a_class) and type(obj) != a_class)
