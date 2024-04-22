"""Functions that implement sorting algorithms."""

__author__ = "730520183"

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    i = 1
    while i < len(x):
        value = x[i]
        position = i
        while position > 0 and x[position - 1] > value:
            x[position] = x[position - 1]
            position -= 1
        x[position] = value
        i += 1
    return None

def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    n = len(x)
    i = 0
    while i < n - 1:
        lowest_index = i
        j = i + 1
        while j < n:
            if x[j] < x[lowest_index]:
                lowest_index = j
            j += 1
        current_value = x[i]
        x[i] = x[lowest_index]
        x[lowest_index] = current_value
        i += 1
    return None

    

