"""One Shot Battleship Exercise"""

__author__: str = "730520183"

secret_row: int = 3
secret_column: int = 2
size_of_grid: int = 4


player_row_input: str = input("Guess a row: ")
player_row = int(player_row_input)
while player_row > size_of_grid or player_row < 1:
     current_row_input: str = input("The grid if only 4 by 4. Try again: ")
     current_row = int(current_row_input)
     player_row = current_row


player_column_input: str = input("Guess a column: ")
player_column = int(player_column_input)
while player_column > size_of_grid or player_column < 1:
        current_column_input: str = input("The grid is only 4 by 4. Try again: ")
        current_column = int(current_column_input)
        player_column = current_column

Blue_box: str = "\U0001F7E6"
Red_box: str = "\U0001F7E5"
White_box: str = "\U00002B1C"
if player_row == 1:
    if player_column == 1:
          print(White_box+3*Blue_box)
          print(4*Blue_box)
          print(4*Blue_box)
          print(4*Blue_box)
    elif player_column == 2:
         print(Blue_box+White_box+2*Blue_box)
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box*4)
    elif player_column == 3:
         print (Blue_box*2+White_box+Blue_box)
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box*4)
    elif player_column == 4:
         print(Blue_box*3+White_box)
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box*4)

if player_row == 2:
    if player_column == 1:
          print(Blue_box*4)
          print(White_box+3*Blue_box)
          print(Blue_box*4)
          print(Blue_box*4)
    elif player_column == 2:
         print(Blue_box*4)
         print(Blue_box+White_box+Blue_box*2)
         print(Blue_box*4)
         print(Blue_box*4)
    elif player_column == 3:
         print(Blue_box*4)
         print(Blue_box*2+White_box+Blue_box)
         print(Blue_box*4)
         print(Blue_box*4)
    elif player_column == 4:
         print(Blue_box*4)
         print(Blue_box*3+White_box)
         print(Blue_box*4)
         print(Blue_box*4)

if player_row == 3:
    if player_column == 1:
        print(Blue_box*4)
        print(Blue_box*4)
        print(White_box+Blue_box*3)
        print(Blue_box*4)
    elif player_column == 2: 
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box+Red_box+Blue_box*2)
         print(Blue_box*4)
    elif player_column == 3:
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box*2+White_box+Blue_box)
         print(Blue_box*4)
    elif player_column == 4:
         print(Blue_box*4)
         print(Blue_box*4)
         print(Blue_box*3+White_box)
         print(Blue_box*4)
if player_row == 4:
     if player_column == 1:
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*4)
          print(White_box+Blue_box*3)
     elif player_column == 2:
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box+White_box+Blue_box*2)
     elif player_column == 3:
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*2+White_box+Blue_box)
     elif player_column == 4:
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*4)
          print(Blue_box*3+White_box)





if player_row == secret_row and player_column == secret_column:
    print("Hit!")
elif player_row == secret_row and not player_column == secret_column:
    print("Close! Correct row, wrong column")
elif player_column == secret_column and not player_row == secret_row:
     print("Close! Correct column, wrong row")
elif player_column != secret_column and player_row != secret_row:
     print("Miss!")





