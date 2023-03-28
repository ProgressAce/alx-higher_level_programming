#!/usr/bin/python3

class Square:
    """Template of a square"""

    def __init__(self, size=0):
        """initialise the square
        Args:
            size(int): the size of the square
        """

        self.size = size

    @property
    def size(self):
        """Returns the size of the square"""

        return (self.__size)

    @size.setter
    def size(self, value):
        """Validate and set a new size for the square
        Args:
            size(int): the size of the square
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square"""

        return (self.__size * self.__size)
