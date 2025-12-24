#!/usr/bin/env python3
"""
Custom object serialization and deserialization using pickle
"""

import pickle


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Returns None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (FileNotFoundError, PermissionError, pickle.PickleError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle.

        Returns None if the file does not exist or is malformed.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, PermissionError,
                pickle.PickleError, EOFError):
            return None
