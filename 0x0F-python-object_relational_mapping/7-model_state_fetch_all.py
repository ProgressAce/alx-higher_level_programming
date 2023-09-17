#!/usr/bin/python3
"""Lists all the states objects from the hbtn_0e_6_usa database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

q = session.query(State).order_by(State.id)  # query object

for state in q:
    print('{}: {}'.format(state.id, state.name))
