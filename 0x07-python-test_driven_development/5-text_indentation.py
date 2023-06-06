#!/usr/bin/python3

"""Module that prints text with 2 new lines if certain chars are found."""


def text_indentation(text):
    """Prints the entire text with an extra new line after certain chars.

    These certain characters are: '.', '?' and ':'. No whitespaces are
    printed at the beginning or at the end of each printed line.

    Arg:
        text(str): the text to be printed.

    Raises:
        TypeError: if the text is not a string.
    """

    if text == '':
        print(text)
        return

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    get_line = False
    line = ''
    for i, char in enumerate(text):
        # whitespaces at the beginning and end of the line should be omitted.
        if char == ' ' and get_line is False:
            continue
        else:
            get_line = True

        if get_line:
            if char == ' ' and text[i + 1] == ' ':
                break
            line += char

        if char in ['.', '?', ':']:
            get_line = False
            line += '\n\n'

    print(line, end='')
