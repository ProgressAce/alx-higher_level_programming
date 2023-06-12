#!/usr/bin/python3

"""Module that defines a class for a square nd inherits from a base class."""


Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a Square and inherits fromparent class Rectangle."""

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns the area of a square."""

        return self.__size ** 2
