#!/usr/bin/python3
"""a square class that presents square"""


class Square():
    """ The intialization of Square class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        return self.__size

    def area(self):
        return (self.__size * self.__size)
