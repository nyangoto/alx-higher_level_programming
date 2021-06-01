#!/usr/bin/python3
"""
Module for save_to_json_file method.
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation.
    Args:
        my_obj (object): object to be serialized.
        filename (str): name of file where string is stored.

    """
    with open(filename, "w",) as j_file:
        json.dump(my_obj, j_file)
