#!/usr/bin/python3
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """Determines if an object is exactly an instance of a class.

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    """

    if type(obj) == a_class:
        return True
    return False
