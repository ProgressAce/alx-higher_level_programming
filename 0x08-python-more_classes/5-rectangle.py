#!/usr/bin/python3

"""Module defining a class for a Rectangle."""


class Rectangle:
    """Blueprints for a Rectangle instance."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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

    def __repr__(self):
        """Represents the rectangle instance as in its code form."""

        rect = '{}'.format(self.__class__.__name__)
        rect += '({}, {})'.format(self.__width, self.__height)

        return rect

    def __del__(self):
        """Prints a message saying bye upon deletion of a rectangle."""

        print('Bye rectangle...')


# rect = Rectangle(4, 6)
# print('rect\'s area: {} and perimeter: {}'.format(rect.area(),
#                                         rect.perimeter()))
# print(rect)
# print(repr(rect))
# rect_cousin = eval(repr(rect))
# print(rect_cousin)
# del rect
