#!/usr/bin/python3
"""In a text file, there is a single character H.
calculate the fewest number of operations"""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op = op + process
            n /= process
        process += 1
    return op
