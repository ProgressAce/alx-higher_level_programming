#!/usr/bin/python3

"""Reads a text file in UTF-8 and prints to stdout."""


def read_file(filename=''):
    """Reads the text file in utf-8 encoding and prints to stdout."""

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')
