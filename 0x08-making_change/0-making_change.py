#!/usr/bin/python3

""" the coin change problem """


def makeChange(coins, total):
    """ find the minimum number of coins
    required to make up a given total amount,
    given a list of coin denominations.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    changes = 0
    coins = sorted(coins, reverse=True)
    i = 0

    while total > 0:
        if i >= len(coins):
            return -1
        coin = coins[i]
        while total >= coin:
            total -= coin
            changes += 1
        i += 1

    return changes
