'''
Simple Enough Hangman Game...is it though???
'''

import random
from wordlist import word_list

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


#get word
def get_word():
    word = random.choice(word_list)
    return word.upper()



#let's play
def play(word):
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    #user prompt to play
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Guess a letter or a word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            #if they have already
            if guess in guessed_letters:
                print("You have already guessed the letter " + guess)

            #if the letter is in the word
            elif guess in list(word):
                guessed_letters.append(guess)

                #check the position of the letter
                list_word = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]

                #replace it in the word the word completion
                for index in indices:
                    list_word[index] = guess


                word_completion = "".join(list_word)
                if "_" not in word_completion:
                    guessed = True
                    break

            #if the letter is not in the word
            else:
                print("Wrong Guess. Try Again.")
                guessed_letters.append(guess)
                tries -= 1

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guessed the word " + guess)

            elif guess == word:
                print("Great Job! " + guess + " is the word!")
                guessed = True
                break
            else:
                print("Wrong Guess! Try Again")
                guessed_words.append(guess)
                tries -= 1
        else:
            print("That is an invalid guess")

        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Maybe next time!")




def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()