#!/usr/bin/python3
"""Return Pascal's triangle of size n"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle"""
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)
        triangle.append(row)

    return triangle
