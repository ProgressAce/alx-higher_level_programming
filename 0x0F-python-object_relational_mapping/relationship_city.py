#!/usr/bin/python3

"""Defines a City model inheriting from SQLAlchemy Base class
and maps to the MySQL table 'cities'."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class City(Base):
    """Represents a city from the mysql database.

    Attributes:
        id: the city's id.
        name: the city's name.
        state_id: the city's state id."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
