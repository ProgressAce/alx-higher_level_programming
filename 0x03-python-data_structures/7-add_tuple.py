#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    first_int = 0
    second_int = 0

    tup_a_size = len(tuple_a)
    tup_b_size = len(tuple_b)

    # validating tuple_a for empty arguments
    if tup_a_size == 0:
        pass
    elif tup_a_size == 1:
        first_int = tuple_a[0]
    else:
        first_int = tuple_a[0]
        second_int = tuple_a[1]

    # sorting tuple_a for empty arguments
    if tup_b_size == 0:
        pass
    elif tup_b_size == 1:
        first_int += tuple_b[0]
    else:
        first_int += tuple_b[0]
        second_int += tuple_b[1]

    return (first_int, second_int)
