#!/usr/bin/python3

""" list all states from the given database"""

import MySQLdb
import sys


def list_states(username, password, database):
    try:
        connection = MySQLdb.connect(host="localhost", user=username,
                                     passwd=password, db=database, port=3306)
        cursor = connection.cursor()
        query = """SELECT cities.id, cities.name, states.name FROM
                 cities INNER JOIN states ON states.id=cities.state_id"""
        cursor.execute(query)
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        connection.close()
    except MySQLdb.Error as err:
        print("MySQL Error:", err)


if __name__ == "__main__":

    """ Entry Point """
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <user> <passwd> <db>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
