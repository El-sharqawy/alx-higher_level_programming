#!/usr/bin/python3
""" From JSON string to Object
"""
import json


def from_json_string(my_str):
    """ a function that turns JSON string
        back to Object
    """
    return json.loads(my_str)
