#!/usr/bin/python3

"""
 function for pascal triangle
"""
def pascal_triangle(n):
    # check if n is less than or equal to 0
    if n <= 0:
        return []

    # initialize the triangle
    triangle = []

    # loop through each row in the triangle
    for i in range(n):
        # initialize the row
        row = []
        c = 1  # starting value for the binomial coefficient

        # fill the row with binomial coefficients
        for j in range(i + 1):
            row.append(c)
            c = c * (i - j) // (j + 1)

        # add the row to the triangle
        triangle.append(row)

    return triangle
