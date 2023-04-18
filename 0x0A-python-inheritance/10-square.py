#!/usr/bin/python3
"""
A module that defines a Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Template for the Square that inherits from Rectangle."""

    def __init__(self, size):
        """Initialising a Square."""

        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size
