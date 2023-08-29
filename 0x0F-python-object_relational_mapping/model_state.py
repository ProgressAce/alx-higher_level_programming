#!/usr/bin/python3
"""Defines a States class modelled from the database states table."""

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
        'mysql+mysqldb://root:root@127.0.0.1:3306/hbtn_0e_6_usa')
Base = declarative_base()


class State(Base):
    """Represents the states table mapped from the hbtn_0e_6_usa database."""

    __tablename__ = 'states'
    id = Column(Integer(), primary_key=True)
    name = Column(String(128), nullable=False)
