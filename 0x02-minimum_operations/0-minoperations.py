#!/usr/bin/python3
"""
calculates the fewest number of operations
needed to result in exactly n H characters
"""


def minOperations(n: int) -> int:
    """
    Calculates  number of operations
    """
    nosOfOperation = 0
    process = 2

    while n > 1:
        if n % process == 0:
            nosOfOperation += process
            n //= process
        else:
            process += 1

    return nosOfOperation
