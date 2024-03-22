"""Dictionary test 5 functions defined in the dictionary.py file."""

__author__: str = "730520183"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance
import pytest 


def test_invert_empty() -> None:
    """Use Case: Test if the function inverted the order in empty dictionary."""
    t: dict[str, str] = {}
    return_value = invert(t)
    assert return_value == {}


def test_invert_one() -> None:
    """Use Case: Test dictionary inverted with large input."""
    t: dict[str, str] = {'a': 'c', 'd': 'r', 'w': 'p', 'f': 'u'}
    return_value = invert(t)
    assert return_value == {'c': 'a', 'r': 'd', 'p': 'w', 'u': 'f'}


def test_invert_edge() -> None:
    """Edge Case for inverted, tets if not unique string can work."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_favorite_color_multiple() -> None:
    """Use case: test if there is not a tie and everyone loves the same color."""
    t: dict[str, str] = {"Marc": "blue", "Ezri": "blue", "Kris": "blue"}
    ret_value = favorite_color(t)
    assert ret_value == "blue"


def test_favorite_color_two() -> None: 
    """Use case: test if there is not a tie."""
    t: dict[str, str] = {"Marc": "green", "Ezri": "green", "Kris": "blue"}
    ret_value = favorite_color(t)
    assert ret_value == "green"


def test_favorite_color_none() -> None:
    """Edge case for test, there is a tie."""
    t: dict[str, str] = {"Marc": "green", "Kris": "blue"}
    ret_value = favorite_color(t)
    assert ret_value == "green"


def test_count_large() -> None: 
    """Use case: test count when there is large input."""
    t: list[str] = ["fish", "cat", "cat", "dog", "cat", "cat"]
    ret_value = count(t)
    assert ret_value == {"cat": 4, "fish": 1, "dog": 1}


def test_count_small() -> None: 
    """Use case: test count when there is small input."""
    t: list[str] = ["fish", "cat", "cat"]
    ret_value = count(t)
    assert ret_value == {"fish": 1, "cat": 2}


def test_count_edge() -> None: 
    """Edge case of testing count, when there is an empty list."""
    t: list[str] = []
    ret_value = count(t)
    assert ret_value == {}


def test_alphabetizer_low_case() -> None: 
    """Use Case: test if it can classify the first letter."""
    t: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    ret_value = alphabetizer(t)
    assert ret_value == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_capital() -> None: 
    """Use case: test if it can classify even capital letter."""
    t: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    ret_value = alphabetizer(t)
    assert ret_value == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_edge() -> None: 
    """Edge case: test there is repeat item."""
    t: list[str] = ["Python", "sugar", "Turtle", "party", "party"]
    ret_value = alphabetizer(t)
    assert ret_value == {'p': ['Python', 'party', 'party'], 's': ['sugar'], 't': ['Turtle']}


def test_update_attendance_exist() -> None: 
    """Use case: if there is already exist date."""
    t: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(t, "Tuesday", "Vrinda")
    assert t == {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa', 'Vrinda']}


def test_update_attendance_new() -> None: 
    """Use case: if there is no that date."""
    t: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(t, "Wednesday", "Kaleb")
    {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa'], 'Wednesday': ['Kaleb']}


def test_update_attendance_no_date_and_name() -> None: 
    """Edge case: No repeat name."""
    t: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(t, "Tuesday", "Alyssa")
    {'Monday': ['Vrinda', 'Kaleb'], 'Tuesday': ['Alyssa']}