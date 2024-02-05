#!/usr/bin/python3
""" a Rectangle subclass named Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square Class"""

    def __init__(self, size):
        """ Initialize square class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
