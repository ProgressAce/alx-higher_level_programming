#!/usr/bin/python3

def safe_print_integer(value):
    try:
        x = int(value)
    except ValueError:
       return False

    print("{:d}".format(x))
    return True
