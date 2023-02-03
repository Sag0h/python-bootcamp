import random
from images import stages as s

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

display = []
for l in chosen_word:
    display.append("_")

finished = False
lives = 6
guessed = 0
while not finished:

    guess = input("Guess a letter: ").lower()

    correct = False

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = chosen_word[i]
            guessed += 1
            correct = True
        
    print(display)

    if not correct: 
        lives -= 1

    print(s[lives])

    if guessed == len(chosen_word):
        finished = True
        print("You win.")
    elif lives == 0:
        print("You lose.")
        finished = True
        