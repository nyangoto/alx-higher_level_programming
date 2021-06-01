#!/usr/bin/python3
"""
Contains definition of class MyInt
"""


class MyInt(int):
    """Definition of class MyInt that inherits from class int"""

    def __eq__(self, other):
        """Overrides equals, inverting it"""
        return int(self) != int(other)

    def __ne__(self, other):
        """Overrides not-equals, inverting it"""
        return int(self) == int(other)
