#!/usr/bin/python3
"""Prints all the state objects that contain the letter 'a' in the database."""

from sqlalchemy import create_engine, or_
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


def main():
    """Entry execution point of the script."""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]))
    session = Session(bind=engine)

    # all records from states(so entire state object) containg letter 'a'.
    q = session.query(State).filter(or_(
        State.name.ilike("a%"),
        State.name.ilike("%a"),
        State.name.ilike("%a%"))
        ).order_by(State.id)

    for col in q:
        print('{}: {}'.format(col.id, col.name))


if __name__ == '__main__':
    main()
