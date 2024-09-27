#!/usr/bin/python3

"""
Island Perimeter
returns perimeter of island
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the
    island described in grid.
    """

    perimeter = 0
    i, j = 0, 0
    cols = len(grid)
    rows = len(grid[0])

    while i < rows:
        while j < cols:
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1
            j += 1
        i += 1
        j = 0

    return perimeter
