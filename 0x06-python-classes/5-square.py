#!/usr/bin/python3
"""defines a Square class"""


class Square:
    """Defines a template for a Square object"""

    def __init__(self, size):
        """Initialises the attributes for the Square
        Args:
            size(int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of the Square object"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Validates and sets a new size value for the Square"""

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the area of a the Square object"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the Square with '#' to stdout,
        If size is 0 the print an empty line
        """
        length = self.__size

        if length == 0:
            print()
        else:
            for h in range(length):
                for w in range(length):
                    print('#', end='')

                print()
