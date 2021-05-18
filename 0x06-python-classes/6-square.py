#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __str__(self):
        """String representation constructor of this square"""
        self.my_print()

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size(int): length of side of the square.
            position(int tuple): position of the square
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Properties for the length of a sise of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: If size < 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for private attribute size.
           Args:
                value: size value to set to.
        """
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for square position.

        Raises:
            TypeError: If value is not tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter function for private attribute position
           Args:
                value: position value to set to.
        """
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
        else:
            raise TypeError("position must be tuple of 2 positive integers")

    def area(self):
        """Area of the square.

        Returns:
            thee size squared.
        """
        return self.__size ** 2

    def my_sprint(self):
        """Returns string representation of this square."""
        ret = ""
        if not self.size:
            return "\n"

        for i in range(self.position[1]):
            ret += "\n"
        for i in range(self.size):
            for j in range(self.position[0]):
                ret += " "
            for j in range(self.size):
                ret += "#"
            ret += "\n"
        return ret

    def my_print(self):
        """Prints this square"""
        print(self.my_sprint(), end="")
