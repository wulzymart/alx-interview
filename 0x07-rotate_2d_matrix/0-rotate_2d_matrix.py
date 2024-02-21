#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    """rotate 2d square matrix in place"""
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # save toplrft
            topleft = matrix[top][left + i]

            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = topleft
        left += 1
        right -= 1
