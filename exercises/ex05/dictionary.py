"""Dictionary exercise 5!"""

__author__: str = "730520183"

def invert(x: dict[str, str]) -> dict[str, str]:
    """Create a new dict to store inverted dictionary!"""
    new_dict = {}
    for key, value in x.items():
        if value in x:
            raise KeyError(f"Value '{value}' already exists as a key in the inverted dictionary.")
        new_dict[value] = key
    return x


def favorite_color(y: dict[str, str])-> str:
    """Return the color happens most frequently!"""
    color_time = {}
    for color in y.values():
        if color in color_time:
            color_time[color] += 1
        else:
            color_time[color] = 1
    most_frequent_color = None
    highest_count = 0
    for color, count in color_time.items():
        if count > highest_count:
            most_frequent_color = color
            highest_count = count

    return most_frequent_color


def count(z: list[str]) -> dict[str, int]:
    """Update counting for the keys!"""
    result_dict: dict[str, int] = {}
    for item in z:
        if item in result_dict:  
            result_dict[item] += 1  
        else:
            result_dict[item] = 1  
    return result_dict



def alphabetizer(a: list[str])-> dict[str, list[str]]:
    """Write down the first letter of every word and sort it."""
    new_dict = {}
    for word in a:
        word_lower = word.lower()
        first = word_lower[0]
        if first in new_dict:
            new_dict[first].append(word_lower)
        else:
            new_dict[first] = [word_lower]
    return new_dict

def update_attendance(attendance: dict[str, list[str]], day_of_week: str, s: str)-> None:
    if day_of_week in attendance:
        if s not in attendance[day_of_week]:
            attendance[day_of_week].append(s)
    else:
        attendance[day_of_week] = [s]
    return None
