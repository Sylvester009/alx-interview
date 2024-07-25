#!/usr/bin/python3
"""
function for pascal triangle
"""


def pascal_triangle(n):
    """check if n is less than or equal to 0
    and iterate through the rows of the triangle
    """
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            c = 1
            for j in range(1, i + 1):
                row.append(c)
                c = c * (i - j) // j
            triangle.append(row)
    return triangle
