#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for column in matrix:
        for row in column:
            if row != column[-1]:
                print("{:d}".format(row), end=" ")
            else:
                print("{:d}".format(row), end="")
        print()
