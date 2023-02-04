from game_data import data as data
import art
import random
import os
import time

def show_vs_art():
    print(art.vs)

def show_logo():
    print(art.logo)

def right_answer_message(score):
    """Returns the message when the answer is right."""
    return "You're right! Current score: "+ str(score)+"."

def wrong_answer_message(score):
    """Returns the message when the answer is wrong."""
    return "Sorry, that's wrong. Final score: "+ str(score)+"."

def pick_random_data():
    return data[random.randint(0, len(data)-1)]

def random_data(o, r_o):
    o = pick_random_data()
    while o['name'] == r_o['name']:
        o = pick_random_data() 
    return o

def choose():
    option = input("Who has more followers? Type 'A' or 'B': ").upper()
    while option != 'A' and option != 'B':
        option = input("Invalid option was entered. Type 'A' or 'B': ").upper()
    return option


def comparation(op1, op2, score):
    if op1['follower_count'] >= op2['follower_count']:
        return True
    else:
        return False

def show_followers(option1, option2):
    print(f"{option1['name']} has {option1['follower_count']} followers.")
    print(f"{option2['name']} has {option2['follower_count']} followers.")

option1 = pick_random_data()
option2 = pick_random_data()
while option2['name'] == option1['name']:
    option2 = pick_random_data() 

score = 0

show_logo()

ok = True

while ok:
    print(f"Compare A: {option1['name']}, {option1['description']}, from {option1['country']}.")
    show_vs_art()
    print(f"Against B: {option2['name']}, {option2['description']}, from {option2['country']}.")

    choice = choose()
    show_followers(option1, option2)
    if choice == 'A':
        if comparation(option1, option2, score):
            score += 1
            time.sleep(3)
            os.system('cls')
            show_logo()
            print(right_answer_message(score))
        else:
            ok = False
    else:
        if comparation(option2, option1, score):
            score += 1
            time.sleep(3)
            os.system('cls')
            show_logo()
            print(right_answer_message(score))
            option1 = option2
        else:
            ok = False
    option2 = random_data(option2, option1)

print(wrong_answer_message(score))

