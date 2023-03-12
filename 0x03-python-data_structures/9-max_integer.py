#!/usr/bin/python3

def max_integer(my_list=[]):

    # empty list validation
    if len(my_list) == 0:
        return None

    max_int = my_list[0]

    for integer in my_list:
        if max_int < integer:
            max_int = integer

    return max_int
