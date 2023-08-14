#!/usr/bin/python3
"""Defines a base class that identifies objects by id."""


class Base():
    """Represents the base class that stores the id of shape classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialises the class instance."""

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
