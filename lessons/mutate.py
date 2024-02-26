"""Mutating functions."""
__author__: str = "730520183"


def manual_append(list: list[int], a: int) -> None:
    """Add a into the list."""
    list.append(a)


def double(list_1: list[int]) -> None:
    """Using the While Loops to double each character in the lists."""
    x = 0
    while x < len(list_1):
        list_1[x] *= 2
        x = x + 1


a: list[int] = [1, 2, 3]
double(a)
print(a)
