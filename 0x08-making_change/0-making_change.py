#!/usr/bin/python3
"""Make changes module"""


def makeChange(coins, total):
    """get minimum number of coins to make amount"""
    # using dynamic programing
    if total <= 0:
        return 0
    count = 0
    i = 0

    coins.sort(reverse=True)
    n = len(coins)
    while total > 0:
        if i >= n:
            return -1
        if total - coins[i] >= 0:
            total -= coins[i]
            count += 1
        else:
            i += 1
    return count
