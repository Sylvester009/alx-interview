#!/usr/bin/python3
"""Game involving the determining of winner
of a game based on the strategic removal
of prime numbers and their multiples from
a set of consecutive integers."""


def isWinner(x, nums):
    """Determines the winner of the Prime Game.
    
    Args:
        x: Number of rounds.
        nums: List of 'n' values for each round.
        
    Returns:
        The name of the player who won the most rounds.
        If no clear winner, return None.
    """
    
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben_wins = 0
    maria_wins = 0

    max_nums = max(nums)
    sieve = [True] * (max_nums + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_nums ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_nums + 1, i):
                sieve[j] = False

    for num in nums:
        prime_count = sum(sieve[2:num + 1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
