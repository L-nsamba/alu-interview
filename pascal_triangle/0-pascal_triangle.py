#!/usr/bin/python3
"""
Module 0-pascal_triangle
Defines a function to generate Pascal’s triangle.
"""


def pascal_triangle(n):
    """
    Generate Pascal’s triangle up to n rows.

    Args:
        n (int): The number of rows of Pascal’s triangle to generate.

    Returns:
        list of lists of int: Pascal’s triangle of n.
        Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # First row

    for i in range(1, n):
        prev_row = triangle[-1]
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # End each row with 1
        triangle.append(row)

    return triangle
