from art import logo
import os

def is_a_operation(operations, symbol):
    """Chequea que symbol este en el diccionario de operaciones disponibles 'operations'."""
    if symbol in operations:
        return True
    return False

def add(n1, n2):
    """Suma n1 con n2"""
    return n1+n2

def sub(n1, n2):
    """Resta n1 con n2"""
    return n1-n2

def mul(n1, n2):
    """Multiplica n1 con n2"""
    return n1*n2

def div(n1, n2):
    """Divide n1 con n2"""
    if n1 == 0 or n2 == 0:
        return "No se puede dividir por 0"
    return n1/n2

def mod(n1, n2):
    """Saca el resto de dividir n1 por n2"""
    return n1%n2

operations = {
    "+": add,
    "-": sub,
    "/": div,
    "*": mul,
    "%": mod
 }



print(logo)

error = True
while error:
    try:
        num1 = float(input("What's the first number?: "))
        error= False
    except:
        print("A non-numeric character was entered, try again.")

error = True
while error:
    try:
        num2 = float(input("What's the second number?: "))
        error= False
    except:
        print("A non-numeric character was entered, try again.")

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
while not is_a_operation(operations, operation_symbol):
    operation_symbol = input("You must enter one of the operations, please try again: ")
answer = operations[operation_symbol](num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
pick = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
while pick != "y" and pick != "n":
    pick = input("Type 'y' or 'n': ").lower()

ok = False

if pick == "y": 
    ok = True

while ok:
    operation_symbol = input("Pick an operation: ")
    while not is_a_operation(operations, operation_symbol):
        for symbol in operations:
            print(symbol)
        operation_symbol = input("You must enter one of the operations from the line above, please try again: ")
    num1 = answer
    
    error = True
    while error:
        try:
            num2 = float(input("What's the next number?: "))
            error= False
        except:
            print("A non-numeric character was entered, try again.")

    answer = operations[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    pick = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    while pick != "y" and pick != "n":
        pick = input("Type 'y' or 'n': ").lower()

    ok = False

    if pick == "y": 
        ok = True
