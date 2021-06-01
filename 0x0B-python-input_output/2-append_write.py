#!/usr/bin/python3
"""
Module for append_write method.
"""


def append_write(filename="", text=""):
    """append_write appends string at the end of a text file.

    Args:
        filename (str): name of file.
            text (str): text to be appended to the file.
        Returns: number of characters written.

    """
    with open(filename, "a", encoding='utf-8') as a_file:
        return a_file.write(text)
