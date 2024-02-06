#!/usr/bin/python3
""" define a class Studentss
"""


class Student:
    """ a class that represents a student"""

    def __init__(self, first_name, last_name, age):
        """ initialize class data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return a dict"""
        return (self.__dict__.copy())
