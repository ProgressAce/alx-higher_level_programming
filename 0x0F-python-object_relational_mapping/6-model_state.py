#!/usr/bin/python3
"""Starts link class to the table in database."""

from sys import argv
from sqlalchemy import (create_engine)
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
