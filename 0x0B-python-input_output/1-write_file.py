#!/usr/bin/python3
"""
Module for write_file method.
"""


def write_file(filename="", text="")
    """write_file writes a string to a text file.
    Args:
        filename (str): name of file.
        text (str): text to be written.

    Return: number of bytes written.

    """
    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
