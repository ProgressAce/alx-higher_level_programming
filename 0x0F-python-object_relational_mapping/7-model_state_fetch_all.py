#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import State, Base
from sys import argv


def main():
    """Entry execution point of the script."""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                             argv[2], argv[3]))
    session = Session(bind=engine)

    q = session.query(State).order_by(State.id)
    for col in q:
        print('{}: {}'.format(col.id, col.name))


if __name__ == '__main__':
    main()
