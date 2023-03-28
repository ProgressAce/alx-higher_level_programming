#!/usr/bin/python3

"""Defines a square class"""

class Square:
    """Describes a square"""

    def __init__(self, size=0):
        """Initialises the square
        Args:
            size(int): the size of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
        """

        if isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        """Returns the current area of the square"""

        return (__self.size * __self.size)
