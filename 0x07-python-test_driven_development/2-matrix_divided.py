#!/usr/bin/python3
"""
This module consists of a function designed to divide the numbers of a matrix
"""

def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix

    Args:
        matrix: list contain lists of integers/floats
        div: number that divides the matrix numbers

    Return:
        a new matrix contains the division results

    Raises:
        TypeError: If the elements of the matrix are not lists
                   If the elements of the lists are not integer/float
                   If the lists of the matrix don't have the same size
                   If the div is not integer/float number
        ZeroDivisionError: If div is zero
    """
def matrix_divided(matrix, div):
    if not type(div) in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    err_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(err_msg)

    length = 0
    err_size = "Each row of the matrix must have the same size"

    for element in matrix:
        if not element or not isinstance(element, list):
            raise TypeError(err_msg)

        if length != 0 and len(element) != length:
            raise TypeError(err_size)

        for num in element:
            if not type(num) in (int, float):
                raise TypeError(err_msg)

        length = len(element)

    myList = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))

    return (myList)
