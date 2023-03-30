#!/usr/bin/python3
"""Defines a square class with an attribute"""


class Square:
    """Describes a square object"""

    def __init__(self, size):
        """Initialises the square
        Args:
            size(int): the size of the square
        """

        self.__size = size
