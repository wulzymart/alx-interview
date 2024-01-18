#!/usr/bin/python3
"""In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n,
write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file."""


def minOperations(n):
    """Gets minimum operations needed to copy and have 'n' 'H'"""
    if n < 2:
        return 0
    grouped_move = 0
    move_count = 2
    n_copy = n
    # root = n ** 0.5
    while (move_count <= n_copy):
        while (n % move_count == 0):
            grouped_move += move_count
            n //= move_count
        move_count += 1
    return grouped_move
