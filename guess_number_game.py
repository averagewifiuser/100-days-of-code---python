'''
In this game, the computer has a number and the player is supposed to guess it.
After three wrong tries, the number is revealed to the player.
The player is allowed to quit the game anytime
'''

import random

def check_entry(user_entry):
    try:
        int(user_entry)
        return True
    except ValueError:
        return False

def play_again():
    response = input("Would you like to play again? y/n: ")
    if response == "y" or response == "Y":
        play_game()
    else:
        print("Bye!")


def play_game():
    number = random.randint(1,100)
    tries = 0

    while tries < 3:
        user_guess = input("What number am I thinking of?... : ")

        _check_entry = check_entry(user_guess)

        while _check_entry == False:
            print("Please enter a number")
            user_guess = input("What number am I thinking of?... : ")
            _check_entry = check_entry(user_guess)


        if int(user_guess) == number:
            print("You got it right!")
            play_again()
            break

        print("That's wrong. Try again")
        tries += 1

        if tries == 3:
            print(f"Game over! The number was {number}")
            play_again()

            
play_game()

