#!/usr/bin/python3
"""Prints all City objects from the database.

Takes three args: <username> <password> <database_name> to connect to the
database hbtn_0e_14_usa.
"""

from sys import argv
from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == '__main__':
    """Access the database and its cities table."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    combo_record = session.query(State.name, City.id, City.name
                                 ).filter(City.state_id == State.id
                                          ).order_by(City.id)

    for rec in combo_record:
        print('{}: ({}) {}'.format(rec[0], rec[1], rec[2]))
