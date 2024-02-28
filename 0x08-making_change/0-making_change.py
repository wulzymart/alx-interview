#!/usr/bin/python3
"""Make changes module"""

import math


def makeChange(coins, total):
    """get minimum number of coins to make amount"""
    # using dynamic programing
    default = total + 1
    dp = [default] * (default)
    dp[0] = 0

    for a in range(1, default):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[total] if dp[total] != default else -1
