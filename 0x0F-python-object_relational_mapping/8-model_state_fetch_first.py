#!/usr/bin/python3
"""Prints the first state object from the hbtn_0e_6_usa database."""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """Access the database and its states table."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print('Nothing')
    else:
        print('{}: {}'.format(first_state.id, first_state.name))
