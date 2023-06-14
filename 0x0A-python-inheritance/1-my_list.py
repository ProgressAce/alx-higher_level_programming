#!/usr/bin/python3

"""Defines a class that inherits from list."""


class MyList(list):
    """Represents a class that inherits from list."""

    def print_sorted(self):
        """Prints the list in sorted order.

        Assumes all the elements of the list to be int.
        """

        print(sorted(self))
