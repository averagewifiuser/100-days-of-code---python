import random


def number_checker(number):
    if int(number) > 10 or int(number) < 1:
        return False
    return True


def game(game_point=3):
    numbers = [x for x in range(11)]
    cpu_points = 0
    player_points = 0
    
    while cpu_points < game_point or player_points < game_point:
        cpu_number = random.choice(numbers)
        player_guess = int(input("What number am I thinking of?: "))

        #verify that the number is between 1 and 10 inclusive
        verify_player_guess = number_checker(player_guess)
        while not verify_player_guess:
            print("Please enter a number between 1 and 10 inclusive")
            player_guess = int(input("What number am I thinking of?: "))
            verify_player_guess = number_checker(player_guess)
        

        if player_guess == cpu_number:
            player_points += 1
            print(f"You got it right. Player has {player_points} points now!")
        else:
            print("You got it wrong!")
            print(f"CPU's number was {cpu_number}")

        if player_points == game_point:
            print("Player won the game!")
            break

        print("\n") #this is a new line

        print("Input a number between 1 anad 10 inclusive")
        player_number = int(input("Enter a number: "))

        verify_player_number = number_checker(player_number)
        while not verify_player_number:
            print("Please enter a number between 1 and 10 inclusive")
            player_guess = int(input("Enter a number: "))
            verify_player_number = number_checker(player_number)

        cpu_guess = random.choice(numbers)

        if cpu_guess == player_number:
            cpu_points += 1
            print(f"CPU got it right! CPU has {cpu_points} points now!")
        else:
            print(f"CPU guessed {cpu_guess}")
            print("CPU got it wrong!!")
        
        print("\n") #this is a new line

        if cpu_points == game_point:
            print("CPU won the game!")
            break


if __name__=='__main__':
    print("Welcome to guess my number game!")
    print("We both take turns guessing each other's number")
    print("Numbers can only be from 1 to 10")
    print("First person to correctly guess three numbers of their opponent wins!")
    print("\n")
    print("Let's play Guess my number!")
    print("\n")

    game()