#!/usr/bin/python3
"""Defines a Square class"""

class Square:
    """Provides a Square object template"""

    def __init__(self, size=0, position=(0,0)):
        """Initialises the Square attributes"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Returns the size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Validates and set a new size value for the Square
        Args:
            value(int): new size for the Square
        """

        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Returns the position of the Square"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Validates and sets a new position for the Square
        Args:
            value(tuple): new position for the Square
        """

        if isinstance(value, tuple) or len(value) == 2:
            self.__position = value
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Returns the area of the Square object"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the Square to stdout with '#' and spaces
        in accordance to its position.
        If size is 0 the print an empty line
        """
        length = self.__size
        space = self.__position[0]

        if length == 0:
            print()
        else:
            for h in range(length):
                print(' ' * space, end='')

                for w in range(length):
                    print('#', end='')

                print()

    def __str__(self):
        """Define the print() representation of the Square"""

        length = self.__size
        space = self.__position[0]

        if length == 0:
            print()
        else:
            for h in range(length):
                print(' ' * space, end='')

                for w in range(length):
                    print('#', end='')

                print()

        return ("")
