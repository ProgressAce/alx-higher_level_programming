#!/usr/bin/python3
"""
A module defining a Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Template for Square that inherits from Rectangle class."""

    def __init__(self, size):
        """Initialising a Square."""

        super().__init__(size, size)
        self.integer_validator('size', size)
        self.__size = size

    def __str__(self):
        """Returns the print() and str() depiction of Square."""

        squ = '[' + self.__class__.__name__ + ']'
        squ += ' ' + str(self.__size) + '/' + str(self.__size)

        return (''.join(squ))

    def area(self):
        """Returns the area of Square."""

        return (self.__size * self.__size)
