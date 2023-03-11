#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    list_range = len(my_list) - 1
    if list_range < 0:
        return my_list

    # validate idx
    if idx < 0:
        return my_list
    if idx > list_range:
        return my_list

    for i in range(list_range + 1):
        if i == idx:
            my_list[i] = element

    return my_list
