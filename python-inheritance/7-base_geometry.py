#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate value as a positive integer.

        Args:
            name (str): the name of the value
            value (int): the value to validate
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
