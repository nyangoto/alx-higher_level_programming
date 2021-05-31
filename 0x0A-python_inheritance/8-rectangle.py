#!/usr/bin/python3
"""
Contains definition of class Reactangle that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(Basegeometry):
    """Defnifition of class Rectangle that inherits from BaseGeometry.
       Attributes:
            width (int): width of the rectangle.
            height (int) height of the rectangle.
    """

    def __init__(self, width, height):
        """Initializes an instance of class Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
