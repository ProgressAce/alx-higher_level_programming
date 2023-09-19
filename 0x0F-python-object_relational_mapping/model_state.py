#!/usr/bin/python3
"""Defines the model mapping for the state table in the MySQL database."""

from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Models a tsble named states of a database.

    Arg:
        id(int): unique integer and primary key of the table.
        name(str): state name.
    """

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(Text(128), nullable=False)
