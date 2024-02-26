"""Functional Battership."""
__author__: str = "730520183"
import random


def input_guess(grid_size: int, row_or_column: str) -> int:
    """Make input for row and column."""
    assert row_or_column == "row" or row_or_column == "column"
    player_input: str = input(f"Guess a {row_or_column}: ") 
    player_input_1 = int(player_input)
    while player_input_1 > grid_size or player_input_1 < 1:
        current_input: str = input(f"The grid is only {grid_size} by {grid_size}. Try again: ")
        current_input_1 = int(current_input)
        player_input_1 = current_input_1
    return player_input_1


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct_guess: bool) -> None: 
    """Print different color of boxes when the current box equals to guess boxes."""
    Blue_box: str = "\U0001F7E6"
    Red_box: str = "\U0001F7E5"
    White_box: str = "\U00002B1C"
    result_box = Red_box if correct_guess else White_box
    row_counter = 1
    while row_counter <= grid_size:
        column_counter = 1
        row_emoji_store = ""
        while column_counter <= grid_size:
            if row_counter == row_guess and column_counter == column_guess: 
                emoji_box = result_box
            else:
                emoji_box = Blue_box
            row_emoji_store = row_emoji_store + emoji_box
            column_counter = column_counter + 1
        print(row_emoji_store)
        row_counter = row_counter + 1


def correct_guess(secret_row: int, secret_column: int, row_guess: int, column_guess: int) -> bool:
    """If correct, then red, incorrect white."""
    if secret_row == row_guess and secret_column == column_guess:
        return True
    else:
        return False


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Count number of turns."""
    turn_count = 1
    won = False

    while turn_count <= 5 and not won:
        print(f"=== Turn {turn_count}/5 ===")
        
        # Get user's guesses for row and column
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        correctness = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, correctness)
        
        if correctness:
            print(f"Hit! You won in {turn_count}/5 turns!")
            won = True
        else:
            print("Miss!")
        turn_count += 1
    if not won:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))