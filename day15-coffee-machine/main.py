MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = [0.01, 0.05, 0.10 ,0.25]
coins_names_plural = ["pennies", "nickles" , "dimes", "quarters"]
# Penny = 0.01, Nickel = 0.05, Dime = 0.10, Quarter = 0.25

def collect_coins():
    print("Please insert coins.")
    cash = 0
    for i in range(len(coins)):
        cash += float(input(f"How many {coins_names_plural[i]}?: "))*coins[i]
    return cash

money = 0.0

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    match choice:
        case "off":
            is_on = False
        case "report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}" + "ml" if resource!="coffee" else f"{resource}: {resources[resource]}g")
            print("Money: $"+str(money))
        case _:
            if choice in MENU:
                introduced_money = collect_coins() 
                ok = True
                for resource in MENU[choice]["ingredients"]:
                    if not resources[resource] - MENU[choice]["ingredients"][resource] >= 0:
                        print(f"Sorry there is not enough {resource}. Money refunded")
                        ok = False
                        break
                if ok:

                    if introduced_money >= MENU[choice]["cost"]:
                        for resource in MENU[choice]["ingredients"]:
                            resources[resource] -= MENU[choice]["ingredients"][resource]
                        change = introduced_money - MENU[choice]["cost"]
                        money += MENU[choice]["cost"]
                        print("Here is $"+ "%.2f" % change +" in change.")
                        print(f"Here is your {choice} ☕ Enjoy!")                    
                    else:
                        print("Sorry that's not enough money. Money refunded")
