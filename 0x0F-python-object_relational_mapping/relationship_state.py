#!/usr/bin/python3

"""Defines a State model inheriting from SQLAlchemy Base class
and maps to the MySQL table 'cities'."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_city import Base, City


class City(Base):
    """Represents a state from the mysql database.

    Attributes:
        id: the state's id.
        name: the state's name.
        cities: the state-city relationship."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')
