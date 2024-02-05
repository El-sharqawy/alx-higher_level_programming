#!/usr/bin/python3
""" a BaseGeometry subclass named Square"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ Square Class inherits from BaseGeometry"""

    def __init__(self, size):
        """ Initialize square class"""
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ str funtion to print with and height"""
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)

    def area(self):
        """ afunction that calculates the area"""
        return self.__size ** 2
