#!/usr/bin/python3
"""
A module defining a class BaseGeometry.
"""


class BaseGeometry:
    """Template for class BaseGeometry."""

    def area(self):
        """Not implemented yet."""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Checks that @value is a natural number.

        Args:
            name(str): the name of the value as a string.
            value(int): the value to check.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        elif not value > 0:
            raise ValueError(f'{name} must be greater than 0')
