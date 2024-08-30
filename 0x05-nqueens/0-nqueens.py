#!/usr/bin/python3
"""This module solves the N-Queens puzzle"""
import sys


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(sys.argv[1])

if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """Recursive function to find possible solutions"""
    if i == n:
        return [a]
    q_positions = []
    for j in range(n):
        if j not in a and i + j not in b and i - j not in c:
            q_positions.extend(
                queens(n, i + 1, a + [j], b + [i + j], c + [i - j]))
    return q_positions


def q_solve(n):
    """Solve function to print the board positions"""
    q_solutions = queens(n)
    for solution in q_solutions:
        print([[i, solution[i]] for i in range(n)])


q_solve(n)
