"""EX01 - Simple Battership - A cute step toward Battelship."""

__author__ = "730520183"
print(__author__)

player_one_input: str = input("Pick a secret boat location between 1 and 4: ")
player_one = int(player_one_input)
if player_one < 1: 
    print("Error!" + str(player_one) + " too low!")
    exit()
if player_one > 4: 
    print("Error!" + str(player_one) + " too high!")  
    exit()
player_two_input: str = input("Guess a number between 1 and 4: ")
player_two = int(player_two_input)
if player_two < 1: 
    print("Error! " + str(player_two) + " too low!")
    exit()
else: 
    if player_two > 4: 
        print("Error!" + str(player_two) + " too high!")
        exit()


Blue_Box: str = "\U0001F7E6"
Red_Box: str = "\U0001F7E5"
White_Box: str = "\U00002B1C"

if player_one == 1: 
    if player_two == 1:
        print(Red_Box + Blue_Box * 3)
    else:
        if player_two == 2: 
            print(Blue_Box + White_Box + Blue_Box * 2)
        else:
            if player_two == 3: 
                print(Blue_Box * 2 + White_Box + Blue_Box)
            else:
                if player_two == 4: 
                    print(Blue_Box * 3 + White_Box)

    
if player_one == 2: 
    if player_two == 2:
        print(Blue_Box + Red_Box + Blue_Box * 2)
    else: 
        if player_two == 1:
            print(White_Box + Blue_Box * 3)
        else:
            if player_two == 3: 
                print(Blue_Box * 2 + White_Box + Blue_Box)
            else:
                if player_two == 4: 
                    print(Blue_Box * 3 + White_Box)

if player_one == 3: 
    if player_two == player_one:
        print(Blue_Box * 2 + Red_Box + Blue_Box)
    else:
        if player_two == 1: 
            print(White_Box + Blue_Box * 3)
        else: 
            if player_two == 2: 
                print(Blue_Box + White_Box + Blue_Box * 2)
            else:
                if player_two == 4: 
                    print(Blue_Box * 3 + White_Box)    

if player_one == 4: 
    if player_two == player_one: 
        print(Blue_Box * 3 + Red_Box)
    else: 
        if player_two == 1: 
            print(White_Box + Blue_Box * 3)
        else: 
            if player_two == 2: 
                print(Blue_Box + White_Box + Blue_Box * 2)
            else: 
                if player_two == 3: 
                    print(Blue_Box * 2 + White_Box + Blue_Box)    
                       

if player_two == player_one: 
    print("Correct! You hit the ship.")
else:
    print("Incorrect! You missed the ship.")