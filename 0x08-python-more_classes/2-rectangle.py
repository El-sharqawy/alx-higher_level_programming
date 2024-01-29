#!/usr/bin/python3
"""
class Rectangle that defines rectangle
"""


class Rectangle():
    """ class Rectangle that defines rectangle"""
    def __init__(self, width=0, height=0):
        """ Initialization with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ get width"""
        return self.__width

    @property
    def height(self):
        """ get height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ set the value of width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ set the value of height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        " calculate Area of the rectangle"
        return self.height * self.width

    def perimeter(self):
        " calculate perimeter of rectangle"
        if self.height == 0 or self.width == 0:
            return (0)
        return ((self.height + self.width) * 2)
