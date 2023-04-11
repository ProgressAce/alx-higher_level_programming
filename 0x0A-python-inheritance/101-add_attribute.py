#!/usr/bin/python3
"""
A module defining a function add_attribute.
"""


def add_attribute(obj, name, value):
    """Adds an attribute to the specified object.

    Args:
        obj(object): the object.
        name(str): the name of the new attribute.
        value: the new atrribute value.

    Raises:
        TypeError: If the attribute cannot be added.
    """

    if not hasattr(obj, '__dict__'):
        raise ValueError("can't add new attribute")

    setattr(obj, name, value)
