#!/usr/bin/python3
"""Experiments with the base class."""


from models.base import Base

if __name__ == '__main__':

    Base()
    print(Base()._Base__nb_objects)  # executes Base() again so 2 will print to sys.stdout
    b2 = Base()
    print(b2)  # <models.base.Base object at ...>
    print(b2.__nb_objects)
