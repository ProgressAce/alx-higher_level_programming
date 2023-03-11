#!/usr/bin/python3
def no_c(my_string):
    new_str = ''

    for i, letter in enumerate(my_string):
        if letter not in 'Cc':
            new_str += letter

    return new_str
