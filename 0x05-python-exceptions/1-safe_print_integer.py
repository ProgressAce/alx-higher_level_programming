#!/usr/bin/python3

def safe_print_integer(value):
    """Prints an integer with {:d}".format().

    Returns: True on success, False otherwise
    """

    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return (False)

    return (True)
