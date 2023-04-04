#!/usr/bin/python3

"""
This module defines function text_indentation(text)
"""


def text_indentation(text):
    """Prints text with 2 new line characters after each of these characters:
        '.', '?' and ':'

    Prints text so that it does not begin or end with any whitespace.

    Args:
        text(str): the text to parse

    Raises:
        TypeError: if text is a non-string
    """

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    new_line = False
    start = 0
    end = 1

    for letter in text:
        # only start new line if line does not start or end with any whitespace
        if letter == ' ' and new_line == False:
            start += 1
            end += 1

        else:
            new_line = True

            if letter in ['.', '?', ':']:
                print(text[start: end])
                print()
                new_line = False
                start = end
                end += 1
            else:
                end += 1

    # for printing a line that does not end with '.', '?' or ':'
    letter = text[end - 2]
    if letter != ' ' and new_line == False:
        print(text[start:end], end='')
