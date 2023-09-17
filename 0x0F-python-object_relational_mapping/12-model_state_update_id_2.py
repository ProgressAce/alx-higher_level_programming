#!/usr/bin/python3
"""Changes the name of a State object from the database.

Takes three args: <username> <password> <database_name> to connect to the
database hbtn_0e_6_usa.
Change the name of the State where id = 2 to New Mexico.
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

    state = session.query(State).get(2)
    state.name = "New Mexico"

    session.add(state)
    session.commit()
