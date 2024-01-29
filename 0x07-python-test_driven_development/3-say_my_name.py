#!/usr/bin/python3
"""
This module consists of a function that outputs a message
"""
def say_my_name(first_name, last_name=""):
    """ Function that prints "My name is <first name> <last name>"

    Args:
        first_name: an input name to print
        last_name: an input name to print

    Return:
        Nothing.

    Raises:
        TypeError: If first_name or last_name is not a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
