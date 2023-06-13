#!/usr/bin/python3

"""Appends a string to the end of a text file(utf-8 encoding)."""


def append_write(filename='', text=''):
    """Appends a string to the end of a text file(utf-8 encoding).

    Arg:
        filename: the text file name.
        text: the string to be written to the text file.

    Return:
        the number of characters written to the text file.
    """

    with open(filename, 'a', encoding='utf-8') as f:
        num_of_chars = f.write(text)

    return num_of_chars
