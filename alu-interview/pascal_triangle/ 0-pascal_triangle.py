#!/usr/bin/python3
"""
This is pascal's triangle problem
"""

def pascal_triangle(n):
    """Return Pascal's triangle as a list of lists of integers.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: Pascal's triangle with n rows.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for row_index in range(1, n):
        prev_row = triangle[row_index - 1]
        row = [1]
        for i in range(1, row_index):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        triangle.append(row)

    return triangle

