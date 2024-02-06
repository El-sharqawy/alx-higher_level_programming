#!/usr/bin/python3
"""
Create object from a JSON file
"""


def load_from_json_file(filename):
    """ a function that creates object from JSON file"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
