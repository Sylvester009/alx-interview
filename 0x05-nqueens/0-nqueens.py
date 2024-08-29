#!/usr/bin/python3
""" this module include handling the queens
game"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)

n = int(sys.argv[1])


def queens(n, i=0, a=[], b=[], c=[]):
    """ find possible positions """
    q_positions = []
    while i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                new_a = a + [j]
                new_b = b + [i + j]
                new_c = c + [i - j]
                q_positions.extend(queens(n, i + 1, new_a, new_b, new_c))
        break
    if i == n:
        q_positions.append(a)
    return q_positions


def q_solve(n):
    """ solve function"""
    x = []
    y = 0
    q_solutions = queens(n, 0)
    while q_solutions:
        q_solution = q_solutions.pop(0)
        while q_solution:
            s = q_solution.pop(0)
            x.append([y, s])
            y += 1
        print(x)
        x = []
        y = 0

q_solve(n)
