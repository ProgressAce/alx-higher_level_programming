#!/usr/bin/python3
"""
Module defining the function lookup.
"""


def lookup(obj):
    """Returns a list of the avaliable attributes and methods
    of an object.
    """

    return (dir(obj))
