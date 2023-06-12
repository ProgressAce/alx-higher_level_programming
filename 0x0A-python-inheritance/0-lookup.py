#!/usr/bin/python3

"""Module returning a list of the available attributes of an object."""


def lookup(obj):
    """Returns a list of an object's attributes.

    Args:
        obj: the object.
    """

    return dir(obj)
