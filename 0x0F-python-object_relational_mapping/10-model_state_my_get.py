#!/usr/bin/python3
"""Print the state object's id using the state name passed as an argument."""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv


def main():
    """Entry execution point of the script."""

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3])
            )
    session = Session(bind=engine)

    q = session.query(State.id).filter(State.name == argv[4])
    print(q[0][0])


if __name__ == '__main__':
    main()
