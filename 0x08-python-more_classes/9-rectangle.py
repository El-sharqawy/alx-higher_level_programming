#!/usr/bin/python3
"""
class Rectangle that defines rectangle
"""


class Rectangle():
    """ class Rectangle that defines rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialization with optional width and height"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect

    @classmethod
    def square(cls, size=0):
        return Rectangle(size, size)

    def area(self):
        """ calculate Area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ calculate perimeter of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ print squares as size as rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""

        return ("\n".join(["".join([str(self.print_symbol)
                for i in range(self.__width)]) for j in range(self.__height)]))

    def __repr__(self):
        """ return a string that represent the rectangle """
        return "Rectnalge({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ delete an instance of rectangle """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
