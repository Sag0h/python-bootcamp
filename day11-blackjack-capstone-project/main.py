from art import logo as logo
import random
import os

def check_ace(player_cards_value, pos): 
    print("What value do you want your Ace to have?")
    error = True
    while error:
        try:
            ace_value = int(input("Type '1' or '11': "))
            while(ace_value != 1 and ace_value != 11):
                ace_value = int(input("Invalid value, type '1' or '11': "))
            error= False
            player_cards_value[pos] = ace_value
        except:
            print("you entered an invalid value.");
            
def check_ace_computer(computer_cards, computer_cards_value):
    if "A" in computer_cards:
        for value in computer_cards_value:
            if value == 1:
                if sum(computer_cards_value) + 10 <= 21:
                    computer_cards_value[computer_cards_value.index(value)] = 11
                
def check_choice():
    choice = input("Type 'y' or 'n': ").lower()
    print(choice)
    while (choice != 'y') and (choice != 'n'):
        choice = input("You typed an invalid option, type 'y' or 'n': ")
    return choice

cards = ["A","2","3","4","5","6","7","8","9","J","Q","K"]
cards_value = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"J":10,"Q":10,"K":10}
ok = True

while ok:
    computer_hits = 0
    player_hits = 0
    players_cards = []
    computer_cards = []

    print("Do you want to play a game of Blackjack?")
    choice = check_choice()
    if choice == "y":
        os.system('cls')
        print(logo)

        player_cards = [random.choice(cards), random.choice(cards)]
        player_cards_value = [cards_value[player_cards[0]], cards_value[player_cards[1]]]
        computer_cards = [random.choice(cards), random.choice(cards)]
        computer_cards_value = [cards_value[computer_cards[0]], cards_value[computer_cards[1]]]
        
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card: {computer_cards[0]}")

        if "A" in player_cards and 10 in player_cards_value:
            print("it's Blackjack!!!") 
            if "A" in computer_cards and 10 in computer_cards_value:
                print(f"Blackjack of Computer! It's a draw, Computer cards: {computer_cards}")
            else:
                while sum(computer_cards_value) < 21 and computer_hits < 5:
                    print("Computer Hit: ")
                    computer_hits += 1
                    if sum(computer_cards_value) < 21:
                        computer_cards.append(random.choice(cards))
                        computer_cards_value.append(cards_value[computer_cards[len(computer_cards)-1]]) 
                        check_ace_computer(computer_cards, computer_cards_value)             
                        print(f"Computer cards: {computer_cards}") 
                if sum(computer_cards_value == 21):
                    print(f"Blackjack of Computer! It's a draw, Computer cards: {computer_cards}")
                else:
                    print("You win.")
        else:
            if 1 in player_cards_value:
                for card in player_cards_value:
                    if card == 1: 
                        check_ace(player_cards_value, player_cards_value.index(1))
            check_ace_computer(computer_cards, computer_cards_value)  
            player_continue = True
            while player_continue and player_hits < 5:
                print("Do you want to get another card? ")
                extra_card = check_choice()
                if extra_card == 'n': 
                    player_continue = False                      
                    print("Computer's turn: ")    
                    if sum(computer_cards_value) < 16 or sum(player_cards_value) > sum(computer_cards_value):
                        computer_hits += 1
                        computer_cards.append(random.choice(cards))
                        computer_cards_value.append(cards_value[computer_cards[len(computer_cards)-1]]) 
                        check_ace_computer(computer_cards, computer_cards_value)             
                    else:
                        print("The computer stands up.")
                        computer_hits = 5                          
                    
                    if sum(player_cards_value) > sum(computer_cards_value) or sum(computer_cards_value) > 21:
                        print(f"Computer cards: {computer_cards}") 
                        print("You win.")
                    else:
                        print(f"Computer cards: {computer_cards}") 
                        print("You lose.")
                else:
                    player_hits += 1
                    new_card = random.choice(cards)
                    player_cards.append(new_card)
                    player_cards_value.append(cards_value[player_cards[len(player_cards)-1]])
                    if player_cards_value[len(player_cards_value)-1] == 1:
                        check_ace(player_cards_value, len(player_cards_value)-1)
              
                    print(f"Your cards: {player_cards}")
                    if sum(player_cards_value) > 21:
                        print("You lose.")
                        player_continue = False
                    elif sum(player_cards_value) == 21:
                        print("it's Blackjack!!!")
                        while sum(computer_cards_value) < 21 and computer_hits < 5:
                            print("Computer's turn: ")
                            computer_hits+=1
                            computer_cards.append(random.choice(cards))
                            computer_cards_value.append(cards_value[computer_cards[len(computer_cards)-1]]) 
                            check_ace_computer(computer_cards, computer_cards_value)                                 
                        if sum(computer_cards_value) == 21:
                            print(f"Blackjack of Computer! It's a draw, Computer cards: {computer_cards}")
                        else:
                            print(f"Computer cards: {computer_cards}") 
                            print("You win.")
                        player_continue = False
                    else:
                        print("Computer's turn: ")
                        if sum(computer_cards_value) < 16 or sum(player_cards_value) > sum(computer_cards_value):
                            computer_hits += 1
                            print(f"Computer cards: {computer_cards}[?]") 
                            computer_cards.append(random.choice(cards))
                            computer_cards_value.append(cards_value[computer_cards[len(computer_cards)-1]]) 
                            check_ace_computer(computer_cards, computer_cards_value)             
                        else:                            
                            print("The computer stands up.")
                            computer_hits = 5                          
    else:
        ok = False