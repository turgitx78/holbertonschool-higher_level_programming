#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class with selective JSON serialization"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes named in attrs
        are included. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result
        return self.__dict__
