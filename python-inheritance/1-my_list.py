#!/usr/bin/python3
"""Defines MyList class"""


class MyList(list):
    """Custom list class that prints a sorted list"""

    def print_sorted(self):
        """Print the list sorted in ascending order"""
        print(sorted(self))
