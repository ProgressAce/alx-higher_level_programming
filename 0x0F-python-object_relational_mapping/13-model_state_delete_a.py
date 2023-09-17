#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a from
the database.

Takes three args: <username> <password> <database_name> to connect to the
database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    """Access the database and its states table."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(or_(
        State.name.ilike("a%"), State.name.ilike("%a%"), State.name.ilike("%a")
        )).delete(synchronize_session='fetch')

    session.commit()
