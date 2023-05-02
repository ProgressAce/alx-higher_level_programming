#!/usr/bin/python3
"""
Module that defines the Base class.
"""


class Base:
    """Template of a Base instance."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of a Base instance."""

        if(id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
