"""One Shot Battleship Exercise."""

__author__: str = "730520183"

secret_row: int = 3
secret_column: int = 2
size_of_grid: int = 4


player_row_input: str = input("Guess a row: ")
player_row = int(player_row_input)
while player_row > size_of_grid or player_row < 1:
    current_row_input: str = input(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: ")
    current_row = int(current_row_input)
    player_row = current_row


player_column_input: str = input("Guess a column: ")
player_column = int(player_column_input)
while player_column > size_of_grid or player_column < 1:
    current_column_input: str = input(f"The grid is only {size_of_grid} by {size_of_grid}. Try again: ")
    current_column = int(current_column_input)
    player_column = current_column

Blue_box: str = "\U0001F7E6"
Red_box: str = "\U0001F7E5"
White_box: str = "\U00002B1C"

  
if player_row == secret_row and player_column == secret_column:
    result_box = Red_box
else:
    result_box = White_box

row_counter = 1

while row_counter <= size_of_grid:
    column_counter = 1
    row_emoji_store = ""
    while column_counter <= size_of_grid:
        if row_counter == player_row and column_counter == player_column:
            # try to see what color is player's choice of row and column. 
            emoji_box = result_box
        else:  # if the the box is not what player chosed, that will be blue.
            emoji_box = Blue_box
            # add emoji results into the blank space
        row_emoji_store = row_emoji_store + emoji_box
        # there is a emoji now, running to produce row 1 column 2 emoji
        column_counter = column_counter + 1
    print(row_emoji_store)
    row_counter = row_counter + 1


if player_row == secret_row and player_column == secret_column:
    print("Hit!")
elif player_row == secret_row and not player_column == secret_column:
    print("Close! Correct row, wrong column.")
elif player_column == secret_column and not player_row == secret_row:
    print("Close! Correct column, wrong row.")
elif player_column != secret_column and player_row != secret_row:
    print("Miss!")