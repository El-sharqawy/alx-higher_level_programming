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

    def to_json(self, attrs=None):
        """ return a dict"""
        obj = self.__dict__.copy()
        if type(attrs) is list:
            for item in attrs:
                if type(item) is not str:
                    return (obj)

            myList = {}

            for iAttr in range(len(attrs)):
                for sAttr in obj:
                    if attrs[iAttr] == sAttr:
                        myList[sAttr] = obj[sAttr]
            return (myList)
        return (obj)

    def reload_from_json(self, json):
        """ a reload method of all Student Attributes"""
        for attr in json:
            self.__dict__[attr] = json[attr]
