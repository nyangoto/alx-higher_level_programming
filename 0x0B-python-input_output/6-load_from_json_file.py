#!/usr/bin/python3
"""
Module for load_from_json_file method.
"""


import json


def load_from_json_file(filename):
    """loads an object from JSON file.
        Args:
            filename (str): name of file.

    """
    with open(filename, "r") as j_file:
        my_obj = json.load(j_file)
        return my_obj
