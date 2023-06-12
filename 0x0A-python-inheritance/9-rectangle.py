#!/usr/bin/python3

"""Module that defines a class for a Rectangle."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a Rectangle class and its objects."""

    def __init__(self, width, height):
        """Initialising the Rectangle with a width and height.

        Arg:
            width: the width of the rectangle.
            height: the height of the rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """Returns the string representation of the Rectangle object."""

        rect = f'[{Rectangle.__name__}]'
        rect += f' {self.__width}/{self.__height}'

        return rect

    def area(self):
        """Returns the area of the Rectangle object."""

        return self.__width * self.__height
