#!/usr/bin/python3

def common_elements(set_1, set_2):

    if set_1 == set() or set_2 == set():
        return set()

    return set.intersection(set_1, set_2)
