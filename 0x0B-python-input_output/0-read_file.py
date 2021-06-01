#!/usr/bin/pyhton3
"""
Module for read_file
"""


def read_file(filename=""):
    """
    Reads text file and prints to STDOUT
    """
    with open(filename, "r", encoding='utf-8') as a_file:
        print("{}".format(a_file.read(), end="")
