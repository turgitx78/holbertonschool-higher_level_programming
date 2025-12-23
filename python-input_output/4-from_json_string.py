#!/usr/bin/python3
"""Return a Python object represented by a JSON string"""


import json


def from_json_string(my_str):
    """Return the Python data structure represented by a JSON string"""
    return json.loads(my_str)
