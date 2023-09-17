#!/usr/bin/python3
"""Prints the State object id of the passed state name argument from datatbase

Takes four args: <username> <password> <database_name> to connect to the
database hbtn_0e_6_usa. The state name to look for, <state_name>.
"""

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

    if not argv[4].isalpha():
        exit()

    state_id = session.query(State.id).filter(
            State.name.like(argv[4])).order_by(State.id).first()

    if state_id is None:
        print('Not found')
    else:
        print(state_id[0])
