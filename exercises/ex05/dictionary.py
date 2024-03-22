"""Dictionary exercise 5!"""

__author__: str = "730520183"


def invert(x: dict[str, str]) -> dict[str, str]:
    """Create a new dict to store inverted dictionary!"""
    new_dict: dict[str, str] = {}
    for key in x:
        value = x[key]
        if value in new_dict:
            raise KeyError(f"Value '{value}' already exists as a key in the inverted dictionary.")
        new_dict[value] = key 
    return new_dict


def favorite_color(y: dict[str, str]) -> str:
    """Return the color that appears most frequently."""
    color_time: dict[str, int] = {}
    for key in y:
        color = y[key]  
        if color in color_time:
            color_time[color] += 1
        else:
            color_time[color] = 1
    most_frequent_color: str = ""
    highest_count = 0
    for color in color_time: 
        count = color_time[color] 
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


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """Write down the first letter of every word and sort it."""
    new_dict: dict[str, list[str]] = {}
    for word in a:
        word_lower = word.lower()
        first = word_lower[0]
        if first in new_dict:
            new_dict[first].append(word)
        else:
            new_dict[first] = [word]
    return new_dict


def update_attendance(attendance: dict[str, list[str]], day_of_week: str, s: str) -> None:
    """Update attendance with name and days."""
    if day_of_week not in attendance:
        attendance[day_of_week] = []
    
    if s not in attendance[day_of_week]:
        attendance[day_of_week].append(s)    
    