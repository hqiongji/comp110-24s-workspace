"""Exercise 4!"""

__author__: str = "730520183"


def all(a: list[int], b: int) -> bool:
    """Check if every elememts in a matches the indicate number b!"""
    if len(a)== 0:
        return False
    
    for elem in a:
        if elem != b:
            return False
    return True 


def max(c: list[int]) -> int:
    """Check every number in the list and return the laregest!"""
    if len(c) == 0:
        raise ValueError("max() arg is an empty List")
    largest = c[0]
    for elem in range(1,len(c)):
        if c[elem] > largest:
            largest = c[elem]
    return largest


def is_equal(d:list[int], e:list[int]) -> bool: 
    """Check if two lists are the same or not!"""
    for elem in d and e:
        if d != e:
            return False
    return True


def extend(f: list[int], g: list[int]) -> None:
    """exntend list after list!"""
    for elem in g:
        f.append(elem)

    f.append(g)




