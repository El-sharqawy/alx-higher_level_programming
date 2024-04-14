#!/usr/bin/python3
"""
script to list all State objects from hbtn_0e_6_usa
Results must be in ASC Order based on ID
"""

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createSession(username, password, database):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()

    if state is None:
        print("Nothing")
    else:
        print(state.id, state.name, sep=": ")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("""Usage: ./7-model_state_fetch_all.py <user> <pwd> <db>""")
        sys.exit(1)

    createSession(sys.argv[1], sys.argv[2], sys.argv[3])
