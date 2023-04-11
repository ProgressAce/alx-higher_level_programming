#!/usr/bin/python3
"""
A module defining the class MyInt that inherits from int.
"""


class MyInt(int):
    """Template for class MyInt, a rebel child class of int."""

    def __eq__(self, value):
        """Returns the bool value != instead of ==."""

        return (self.real != value)

     def __ne__(self, value):
        """Override != operator with == behavior."""

        return self.real == value
