#!/usr/bin/python3
"""Defining a class for a Rectangle."""
from models.base import Base


class Rectangle(Base):
    """Representing a Rectangle object."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation of a rectangle.

        Arg:
            width: the rectangle's width.
            height: the ractangle's height.
            x: the rectangle's position on the x-axis.
            y: the rectangle's position on the y-axis.
            id: the id of the rectangle object."""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Returns the string representation of the rectangle."""

        rect = '[{}] ({})'.format(self.__class__.__name__, self.id)
        rect += '{}/{} - {}/{}'.format(self.__x, self.__y, self.__width,
                                       self.__height)
        return rect

    def display(self):
        """Displays the rectangle instance using #.

        Takes the x and y axis positions into account."""

        for i in range(self.__y):  # for its y-axis position
            print()

        for i in range(self.__height):  # for its height
            print(' '*self.__x + '#'*self.__width)  # for its x-axis position and width length

    def update(self, *args):
        """Changes the value of each argument.

        Changes the values according to the argument order.

        Arg:
            args: the sequence of ordered arguments."""

        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            if i == 1:
                self.__width = arg
            if i == 2:
                self.__height = arg
            if i == 3:
                self.__x = arg
            if i == 4:
                self.__y = arg
