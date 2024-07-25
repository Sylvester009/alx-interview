#!/usr/bin/python3
"""
 function for pascal triangle
"""
def pascal_triangle(n):
    """
    check if n is less than or equal to 0
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = []
        c = 1
        for j in range(i + 1):
            row.append(c)
            c = c * (i - j) // (j + 1)
        triangle.append(row)
    return triangle
