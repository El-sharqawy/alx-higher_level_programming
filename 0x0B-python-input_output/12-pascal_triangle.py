#!/usr/bin/python3
""""
Pascal's Triangle
"""


def pascal_triangle(n):
    """ def for Pascal's Triangle"""
    if n <= 0:
        return ([])

    myTriangles = [[1]]
    while len(myTriangles) != n:
        trio = myTriangles[-1]
        temp = [1]
        for i in range(len(trio) - 1):
            temp.append(trio[i] + trio[i + 1])
        temp.append(1)
        myTriangles.append(temp)
    return myTriangles
