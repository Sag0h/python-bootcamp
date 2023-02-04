import random
from art import logo as logo
import os

def play(lives, the_number):
    """This function contains all the logic of the game"""
    did_guess = False
    while lives > 0 and not did_guess:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == the_number:
            print(f"You got it! The answer was {the_number}.")
            did_guess = True
        else:
            lives -= 1
            if guess > the_number:
                print("Too high.")
            else:
                print("Too low.")
            if lives > 0:
                print("Guess again.")
    if not did_guess:
        print("You've run out of guesses, you lose.")
        print(f"The answer was {the_number}.")


def set_difficulty():
    """This function sets the difficult in easy or hard, returns the number of tries the player has"""
    difficulty_chosen = input("Choose a difficulty. Type 'easy' or 'hard': ")
    while(difficulty_chosen != "easy" and difficulty_chosen != "hard"):
        difficulty_chosen = input("You entered an invalid option. Type 'easy' or 'hard': ")
    return 10 if difficulty_chosen == "easy" else 5

print(logo)
play_loop = "y"
while play_loop == "y":
    
    the_number = (random.randint(1,100))
    print("I'm thinking a number between 1 and 100.")

    difficulty = set_difficulty()
    play(difficulty, the_number)

    play_loop = input("\nDo you want to play again?\n Type 'y' or 'n': ")
    if play_loop != "n" and play_loop != "y":
        play_loop = input("An invalid option was entered, if you want to play again type 'y' else type 'n': ")
    if play_loop == "y":
        os.system('cls')