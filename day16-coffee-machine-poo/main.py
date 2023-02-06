from menu import *
from money_machine import *
from coffee_maker import *

def exists_drink(order, menu):
    return menu.find_drink(order) != None 

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    order = input(f"What would you like? ({menu.get_items()}): ")
    if order == "off":
        is_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    elif exists_drink(order, menu):
        order = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)
        
            