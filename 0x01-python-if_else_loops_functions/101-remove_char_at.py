#!/usr/bin/python3
def remove_char_at(str1, n):
    new_str = ''

    for pos, letter in enumerate(str1):
        if pos != n:
            new_str += letter

    return new_str
