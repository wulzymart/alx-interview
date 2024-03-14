#!/usr/bin/python3
"""is winner.
"""


def SieveOfEratosthenes(n):

    # Create a boolean array
    # "prime[0..n]" and initialize
    #  all entries it as true.
    # A value in prime[i] will
    # finally be false if i is
    # Not a prime, else true.
    primes = []
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes


def isWinner(x, nums):
    """checks winner based on x moves
    """
    if x < 1 or not nums:
        return None
    maria, ben = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(1, n + 1)]
    primes[0] = False
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        count = len(list(filter(lambda x: x, primes[0: n])))
        ben += count % 2 == 0
        maria += count % 2 == 1
    if maria == ben:
        return None
    return 'Maria' if maria > ben else 'Ben'
