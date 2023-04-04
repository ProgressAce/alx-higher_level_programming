#!/usr/bin/python3

"""This module defines function say_my_name(first_name, last_name="")"""


def say_my_name(first_name, last_name=""):
    """Prints: My name is <first name> <last name>

    Raises:
        TypeError: if first_name or last_name is a non-string
    """

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')

    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print('My name is {} {}'.format(first_name, last_name))
