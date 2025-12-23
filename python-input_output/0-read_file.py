#!/usr/bin/python3
"""Reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
