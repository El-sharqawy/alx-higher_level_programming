#!/usr/bin/python3
"""
Append to a file
"""


def append_write(filename="", text=""):
    """ a function that appends to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
        return chars_added
