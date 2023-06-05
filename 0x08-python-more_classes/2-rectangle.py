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
