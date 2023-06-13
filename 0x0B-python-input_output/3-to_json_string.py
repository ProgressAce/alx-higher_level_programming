#!/usr/bin/python3
"""Returns a JSON string representation from a python object."""

import json


def to_json_string(my_obj):
    """Translates a python object to a JSON string.

    Arg:
        my_obj: the python object to convert to json .

    Return:
        a json string object.
    """

    return json.dumps(my_obj)
