#!/usr/bin/python3

""" list all states from the given database"""

import MySQLdb
import sys


def list_states(username, password, database, user_input):
    try:
        connection = MySQLdb.connect(host="localhost", user=username,
                                     passwd=password, db=database, port=3306)
        cursor = connection.cursor()
        query = """SELECT cities.name FROM cities INNER JOIN states ON
                states.id = cities.state_id WHERE states.name=%s"""
        cursor.execute(query, (user_input, ))
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        connection.close()
    except MySQLdb.Error as err:
        print("MySQL Error:", err)


if __name__ == "__main__":

    """ Entry Point """
    if len(sys.argv) != 5:
        print("Usage: ./0-select_states.py <user> <passwd> <db> <city>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    user_input = sys.argv[4]

    list_states(username, password, database, user_input)
