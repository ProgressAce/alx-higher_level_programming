#!/usr/bin/python3

"""This module defines a class called Rectangle"""


class Rectangle:
    """A class representing a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of the rectangle object"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """validates and sets the width of the rectangle object"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """returns the height of the rectangle object"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """validates and sets the height of the rectangle object"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """returns the area of the rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle object"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """returns a printable form of the rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return ('')

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append('#')

            if i != self.__height - 1:  # the string should not end with a new line
                rect.append('\n')

        return (''.join(rect))