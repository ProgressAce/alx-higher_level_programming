#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None

    # the range of mylist
    list_range = len(my_list) - 1
    if list_range < 0:
        return None

    if idx > list_range:
        return None
    else:
        return my_list[idx]
