#!/usr/bin/python3

"""Module defining a class for a Rectangle."""


class Rectangle:
    """Blueprints for a Rectangle instance."""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""

        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle."""

        if self.__width == 0 or self.__height == 0:
            return 0

        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """Representing the rectangle instance as a string with char #"""

        if self.__width == 0 or self.height == 0:
            return ''

        rect = ''
        for i in range(self.__height):
            rect += '#' * self.__width

            if not i == self.__height - 1:
                rect += '\n'

        return rect

# Rect = Rectangle(4, 6)
# print('Rect\'s area: {}'.format(Rect.area()))
# print('Rect\'s perimeter: {}'.format(Rect.perimeter()))
# print(Rect)
