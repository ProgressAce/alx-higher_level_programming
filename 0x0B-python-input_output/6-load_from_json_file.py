#!/usr/bin/python3
"""Creates a python object from a JSON file."""

import json


def load_from_json_file(filename):
    """Creates a python object from a JSON file.

    Uses JSON string deserialisation to convert the string to a object.
    File permission exceptions and json string not representing an
    object exceptions are not handled.

    Arg:
        filename: the json formatted file's name.

    Return:
        the python object translated from a json file.
    """

    with open(filename, 'r', encoding='utf-8') as f:
        obj = json.loads(f.read())
        return obj
