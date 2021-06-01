#!/usr/bin/python3
"""
Contains definition for the class Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of class square that inherits from class Rectangle"""

    def __init__(self, size):
        """Initializes instance of the class Square"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Method for computing Square area"""
        return self.__size ** 2

    def __str__(self):
        """Returns string representation of an instance of class square"""
        return "[{}] {}/{}".format(type(self).__name, self.__size,
                                   self.__size)
