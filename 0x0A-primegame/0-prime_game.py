#!/usr/bin/python3

""" Python program to print all
primes smaller than or equal to
n using Sieve of Eratosthenes
"""

def SieveOfEratosthenes(n):
    """Returns a list of booleans indicating whether numbers are prime up to n"""
    prime = [True for _ in range(n+1)]
    p = 2
    while (p * p <= n):
        if prime[p]:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime[0], prime[1] = False, False
    return prime

"""
Determine the winner of the Prime Game after x rounds
"""

def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    max_nums = max(nums)
    prime = SieveOfEratosthenes(max_nums)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        primes_count = sum(prime[2:n+1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
