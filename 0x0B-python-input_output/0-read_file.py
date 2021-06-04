#!/usr/bin/pyhton3
"""
Module for read_file
"""


def read_file(filename=""):
    """
    Reads text file and prints to STDOUT
    """

    with open(filename, mode="r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
