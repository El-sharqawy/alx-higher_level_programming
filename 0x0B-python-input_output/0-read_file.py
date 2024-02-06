#!/usr/bin/python3
"""
Read File
"""


def read_file(filename=""):
    """ a function to read file and print it to ouput"""
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
