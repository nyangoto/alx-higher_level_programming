#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of ints"""
    for row in matrix:
        for i in row:
            if i != row[-1]:
                print("{:d}".format(i), end="")
            else:
                print("{:d}".format(i), end="")
        print()
