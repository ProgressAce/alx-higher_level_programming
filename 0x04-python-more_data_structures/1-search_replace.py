#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list == []:
        return my_list

    if search == None or replace == None:
        return my_list

    new_list = my_list.copy()

    for i, item in enumerate(my_list):
        if item == search:
            new_list[i] = replace

    return new_list
