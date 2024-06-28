#!/usr/bin/python3
"""
0-pascal_triangle
"""

def pascal_triangle(n):
    """
    Returns a list of integers
    representing the Pascal Triangle of n
    returns empty list if n <= 0
    """
    tab = []
    if n <= 0:
        return tab

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = tab[i-1][j-1] + tab[i-1][j]
        tab.append(row)
    return tab

