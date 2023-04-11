#!/usr/bin/python3
"""
A module defining a class Rectangle, which inherits from
class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Template for class Rectangle, a subclass of class BassGeometry."""

    def __init__(self, width, height):
        """Initialisation of Rectangle object.

        Width and height must be positive integers. Uses the baseclass
        method @integer_validator to validate.

        Args:
            width(int): the width of the rectangle.
            height(int): the height of the rectangle.

        Raises:
            TypeError: if width or height are not integers.
            ValueError: if width or height are not greater than 0.
        """

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
