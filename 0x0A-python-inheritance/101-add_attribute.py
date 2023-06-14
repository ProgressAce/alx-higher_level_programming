#!/usr/bin/python3

"""Module that adds a new attribute to an object if it is possible."""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it is possible.

    Arg:
        obj: the object to add the new attribute to.
        name: the name of the new attribute.
        value: the value of the new attribute.
    
    Raises:
        TypeError: if the object can’t have new attribute.
    """

    if obj not in vars().values():
        raise TypeError('can\'t add new attribute')
    setattr(obj, name, value)
