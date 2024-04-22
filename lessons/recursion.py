"""Create Recursive FUnction!"""


def f(n: int, k: int) -> int:
    """Recrursive function for n*k."""
    if n == 0:
        return 0
    else:
        return k + f(n - 1, k)