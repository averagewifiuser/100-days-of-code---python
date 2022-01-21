from ipaddress import v4_int_to_packed
import math
import random 

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter


    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    
    def get_move(self, game):
        #get a random valid spot
        square = random.choice(game.available_moves())
        return square



class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            #checks to see if the correct inputs are entered
            try:
                val = int(square)
                #checking to see if the square is available
                if val not in game.available_moves():
                    print(game.available_moves())
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try Again!')

        return val
