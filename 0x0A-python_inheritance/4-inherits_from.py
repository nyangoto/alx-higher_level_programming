#!/usr/bin/python3
"""
Module for is_same_class method
"""


def inherits_from(obj, a_class):
    """Method for comparing object classes

    Args:
        obj (unknown): object whose type is to be checked.
        a_class (str): class criteria to validate.

    Return:
        True if obj isinstance of a_class/ class that inherits from it.
        otherwise False

    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
