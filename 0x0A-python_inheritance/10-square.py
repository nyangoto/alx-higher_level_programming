#!/usr/bin/python3
"""
Contains the definition of the class Square.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class Square that inherits from class Rectangle"""

    def __init__(self, size):
        """Initialise an instance of the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
