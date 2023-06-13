#!/usr/bin/python3
"""Translates a json string object to a python data object."""

import json


def from_json_string(my_str):
    """Translates a JSON formatted string to a python object.

    Arg:
        my_str: the json string to convert.

    Return:
        a python object converted from the provided json string.
    """

    return json.loads(my_str)
