#!/usr/bin/python3
"""Prints the first state object from the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


def main():
    """Entry execution point of the script."""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    q = session.query(State.id, State.name).first()
    if not q:
        print('Nothing')
    else:
        print('{}: {}'.format(q[0], q[1]))  # q points to a tuple of the record


if __name__ == '__main__':
    main()
