#!/usr/bin/python3
"""
script to list all State objects from hbtn_0e_6_usa
Results must be in ASC Order based on ID
"""

import sys
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def createSession(username, password, database):
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State.name, City.id, City.name)
    filter_query = (City.state_id == State.id)

    for instance in query.filter(filter_query):
        print("{}: ({}) {}".format(instance[0], instance[1]), instance[2])

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("""Usage: ./11-model_state_insert.py <user> <pwd> <db>""")
        sys.exit(1)

    createSession(sys.argv[1], sys.argv[2], sys.argv[3])
