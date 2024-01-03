#!/usr/bin/python3
"""Module containing solution for pascal triangle"""


def pascal_triangle(n):
    """returns matrix of pascal triangle"""
    if n <= 0:
        return []
    triangle = [[1]]  # first line is always 1
    for i in range(1, n):
        row = [1]  # rows start with 1
        prev = triangle[i - 1]
        for j in range(1, i):
            row.append(prev[j - 1] + prev[j])
        row.append(1)  # row ends with 1
        triangle.append(row)
    return triangle
