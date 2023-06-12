#!/usr/bin/python3

"""Module that defines class MyInt that inherits from `int`."""


class MyInt(int):
    """Represents an int object with differences in its equality values."""

    def __eq__(self, value):
        """Returns the opposite of the usual == operator."""

        return self.real != value

    def __ne__(self, value):
        """Returns the opposite of the usual != operator."""

        return self.real == value
