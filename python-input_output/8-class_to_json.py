#!/usr/bin/python3
"""Return the dictionary description of an object for JSON serialization"""


def class_to_json(obj):
    """Return the dictionary representation of obj"""
    return obj.__dict__
