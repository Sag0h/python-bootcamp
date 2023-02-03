from art import logo as logo
import os

print(logo)
print("Welcome to the secret auction program.")

people = {}

ok=True

while ok:
    name = input("What's your name?: ")
    bid = float(input("What's your bid?: $"))

    people[name] = bid

    print("Are there any other bidders?")
    next = input("Type 'yes' or 'no'.\n")
    while (next != "yes") & (next != "no"):
        print("An invalid option was entered, please try again")
        next = input("Type 'yes' or 'no'./n")
    if next == "no":
        ok = False
    os.system('cls')

winner = ""
max = 0
for p in people:
    if people[p] > max:
        max = people[p]
        winner = p

print(f"The winner is {winner} with a bid of ${max}.")
