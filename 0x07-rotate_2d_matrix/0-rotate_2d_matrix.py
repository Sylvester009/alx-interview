#!/usr/bin/python3
"""
Rotate 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix 90 degrees clockwise in place
    without returning anything.
    """
    n = len(matrix)
    
    # Loop over each layer, starting from the outer layer, inwards
    for i in range(n // 2):
        # Define the last index of the current layer
        k = n - i - 1
        # Iterate over each element in the layer
        for x in range(i, k):
            y = n - 1 - x
            # Perform the 4-way rotation swap
            tmp = matrix[i][x]
            matrix[i][x] = matrix[y][i]
            matrix[y][i] = matrix[k][y]
            matrix[k][y] = matrix[x][k]
            matrix[x][k] = tmp
