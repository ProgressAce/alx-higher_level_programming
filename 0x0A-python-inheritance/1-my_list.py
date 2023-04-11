#!/usr/bin/python3
"""
Module defining class MyList that inherits from list
"""


class MyList(list):
    """A child class of list that uses its methods to
    act as a list object: with a unique print method
    """

    def __init__(self):
        """initialisation of object"""
        self.__my_list = super()

    def print_sorted(self):
        """Prints the my_list list in a sorted ascending format"""

        list_copy = self.__my_list.copy()
        list_copy.sort()

        print(list_copy)
