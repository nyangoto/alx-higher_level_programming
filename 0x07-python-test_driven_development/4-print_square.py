#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Methos for printing square with # characters.

    Args:
        size: length of square side of type int.

    Raises:
        TypeError: if size is not int.
        ValueError: if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0.")

    print((("#" * size + "\n") * size), end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
