#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Print integers of a list in reversed order"""
    if my_list:
        for i in range(len(my_list) - 1, -1, -1):
            print("{:d}".format(my_list[i]))
