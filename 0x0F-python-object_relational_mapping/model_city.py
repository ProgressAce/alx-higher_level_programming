#!/usr/bin/python3
"""Defines a class that models the cities table in the database."""

from sqlalchemy import Column, Integer, Text, ForeignKey
from model_state import Base


class City(Base):
    """Models after a table named cities in a database.

    Arg:
        id(int): the unique integer primary key.
        name(str): the name of the city.
        state_id(int): the state name of the city.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
#    state = relationship('State', backref='cities')
