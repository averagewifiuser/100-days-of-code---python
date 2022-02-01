''' 
A rock-paper-scissor game. You play with the computer.
Pretty basic
'''
import random

def check_winner(npc, user):
    #rock beats scissors
    if (npc == 0 and user == 2) or (npc == 1 and user == 0) or (npc == 2 and user == 1):
        print("Computer Wins")
        return "npc"

    elif (npc == 2 and user == 0) or (npc == 0 and user == 1) or (npc == 1 and user == 0):
        print("Player Wins")
        return "user"
    else:
        print("Draw")
        return "draw"

def check_entry(user_entry):
    if user_entry.isdigit() and int(user_entry) in range(1,4):
        return True
    return False


def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_points = 0
    npc_points = 0


    while user_points < 3 and npc_points < 3:
        print("\nRock, Paper, Scissors")
        user_choice = input("Enter 1 for rock, 2 for paper and 3 for scissors: ")

        _check_entry = check_entry(user_choice)
        while _check_entry == False:
            user_choice = input("Enter 1 for rock, 2 for paper and 3 for scissors: ")
            _check_entry = check_entry(user_choice)

        
        npc_choice = choices.index(random.choice(choices))
        winner = check_winner(npc_choice, int(user_choice)-1)

        if winner == "user":
            user_points += 1
        elif winner == "npc":
            npc_points += 1
            
        print(f"\n User Points: {user_points} \n Computer Points: {npc_points}")

        if user_points == 3:
            print("User wins the game!")
            
        if npc_points == 3:
            print("Computer wins the game!")
            
            
play_game()