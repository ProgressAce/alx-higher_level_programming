#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """executes a function safely"""

    try:
        result = fct(*args)
        return result
    except (IndexError, ValueError, TypeError, ZeroDivisionError) as err:
        print('Exception: {}'.format(err), file=sys.stderr)
        return None
