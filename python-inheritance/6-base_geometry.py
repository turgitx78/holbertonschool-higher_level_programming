#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raise an Exception indicating area is not implemented"""
        raise Exception("area() is not implemented")
