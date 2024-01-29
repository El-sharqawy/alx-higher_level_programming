#!/usr/bin/python3
"""
This module comprises a function that generates a square using the character # and prints it.
"""

def print_square(size):
    """ Function that prints a square with the character #

    Args:
        size: size of the square to be printed

    Return:
        Nothing.

    Raises:
        TypeError: If size is not an integer number
        ValueError: "size must be >= 0"

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
