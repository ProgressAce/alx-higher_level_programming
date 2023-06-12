#!/usr/bin/python3

"""Module that defines a class for Base Geometry."""


class BaseGeometry:
    """Representation of a class for Base Geometry."""

    def area(self):
        """Not yet implemented."""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the passed value.

        Name is assumed to always be a string. Value should be an
        integer and greater than 0.

        Arg:
            name(str): the name referring to the value.
            value: the value to validate.
        """

        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value < 1:
            raise ValueError('{} must be greater than 0'.format(name))
