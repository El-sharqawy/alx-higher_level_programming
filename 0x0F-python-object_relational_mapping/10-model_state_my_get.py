#!/usr/bin/python3
"""
script to list all State objects from hbtn_0e_6_usa
Results must be in ASC Order based on ID
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createSession(username, password, database, searchFor):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == (searchFor,))

    try:
        print(state[0].id)
    except IndexError:
        print("Not found")


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("""Usage:./10-model_state_my_get.py <user> <pwd> <db> <state>""")
        sys.exit(1)

    createSession(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
