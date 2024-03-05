#!/usr/bin/python3
"""Module containing grid perimeter calculation"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid:

    grid is a list of list of integers:
    0 represents a water zone
    1 represents a land zone
    One cell is a square with side length 1
    Grid cells are connected horizontally/vertically (not diagonally).
    Grid is rectangular, width and height don’t exceed 100
    """
    width = len(grid[0])
    height = len(grid)
    perimeter = 0
    for h in range(height):
        for w in range(width):
            if grid[h][w] == 1:
                # handle the top
                if not (h != 0 and grid[h - 1][w] == 1):
                    perimeter += 1
                # handle the bottom
                if not (h != height - 1 and grid[h + 1][w] == 1):
                    perimeter += 1
                # handle the left
                if not (w != 0 and grid[h][w - 1] == 1):
                    perimeter += 1
                # handle the right
                if not (w != width - 1 and grid[h][w + 1] == 1):
                    perimeter += 1
    return perimeter
