"""Summing the elements of a list using different loops.""" 

__author__: str = "730520183"


def w_sum(vals: list[float]) -> float: 
    """Sum up every numbe in the list using While."""
    idx = 0
    sum = 0.0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float: 
    """Sum up every elements in the list."""
    sum = 0.0
    for elem in vals:
        sum = sum + elem
    return sum


def f_range_sum(vals: list[float]) -> float: 
    """Sum up every elements in the range."""
    sum = 0.0
    for elem in range(0, len(vals)):
        sum = sum + vals[elem]
    return sum