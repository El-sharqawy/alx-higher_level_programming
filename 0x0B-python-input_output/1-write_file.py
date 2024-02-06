#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
    """ a function that writes to a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
