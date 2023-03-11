#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()

    # get the range of copied list
    list_range = len(list_copy) - 1
    if list_range < 0:
        return list_copy

    # validate idx
    if idx < 0 or idx > list_range:
        return list_copy

    list_copy[idx] = element
    return list_copy
