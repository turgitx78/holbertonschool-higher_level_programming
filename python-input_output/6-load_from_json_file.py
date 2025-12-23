#!/usr/bin/python3
"""Create an object from a JSON file"""


import json


def load_from_json_file(filename):
    """Return the Python object represented by a JSON file"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
