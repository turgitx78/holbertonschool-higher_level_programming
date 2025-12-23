#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle"""

    def __init__(self, size):
        """Initialize square with validated size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size * self.__size
