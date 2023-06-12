#!/usr/bin/python3

"""Module that defines a class for a square nd inherits from a base class."""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a Square and inherits fromparent class Rectangle."""

    def __init__(self, size):
        """Initialises a square with its size.

        Arg:
            size: the length of the square.
        """

        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns the string representation of a square."""

        sq = '[{}]'.format(self.__class__.__name__)
        sq += ' {}/{}'.format(self.__size, self.__size)

        return sq

    def area(self):
        """Returns the area of a square."""

        return self.__size ** 2
