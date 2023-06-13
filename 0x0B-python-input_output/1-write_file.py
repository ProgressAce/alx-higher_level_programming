#!/usr/bin/python3

"""Writes a string to a text file(utf-8 encoding)."""


def write_file(filename='', text=''):
    """Writes a string to a text file(utf-8 encoding).

    Arg:
        filename: the text file name.
        text: the string to be written to the text file.

    Return:
        the number of characters written to the text file.
    """

    with open(filename, 'w', encoding='utf-8') as f:
        num_of_chars = f.write(text)

    return num_of_chars
