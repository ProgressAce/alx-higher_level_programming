#!/usr/bin/python3
"""Lists the State objects containing the letter 'a' from the database.

The database used is hbtn_0e_6_usa. The letter can be any position in the
state name.
"""

from sys import argv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                       .format(argv[1], argv[2], argv[3]))
Session = sessionmaker(bind=engine)
session = Session()

q = session.query(State).filter(or_(
    State.name.like('%a'), State.name.like('%a%'))
    ).order_by(State.id)

for state in q:
    print('{}: {}'.format(state.id, state.name))
