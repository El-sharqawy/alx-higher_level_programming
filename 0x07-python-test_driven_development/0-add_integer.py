#!/usr/bin/python3
"""
This module consists of a function designed to add two numbers.
"""

def add_integer(a, b=98):
    """ a function designed to add two numbers

    Args:
        a: first number passed to the function
        b: second number passed to the function

    Return:
        addition of the given two numbers

    Raises:
        TypeError: If a or b are not integer/float numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return (a + b)
