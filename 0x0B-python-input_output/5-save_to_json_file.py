#!/usr/bin/python3
"""Writes a python object to a text file, using json serialisation."""

import json


def save_to_json_file(my_obj, filename):
    """Writes a python object to a text file.

    Uses JSON string serialisation to convert the object to a string.
    File permission and unable to serialise to json string exceptions
    are not handled.

    Arg:
        my_obj: the object to write to the text file.
        filename: the file's name to write @my_obj to.
    """

    with open(filename, 'w', encoding='utf-8') as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
