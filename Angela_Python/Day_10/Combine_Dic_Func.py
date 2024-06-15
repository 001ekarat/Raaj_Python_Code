# Calculater
from art import logo
#Add 
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1 , n2):
    return n1 - n2

# Multiply
def multiply(n1 , n2):
    return n1 * n2

# Divide
def divide(n1 , n2):
    return n1 / n2

# Store these function inside dictianary where keys are Symbol and values are names of the functions.

operations = {                                          
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# function = operations["*"]         This function act as the multiply function , change to + Know this function act as a add function. 
# function(2,3)
# print(function(2,3))
#print(function(2,3)= operations["*"])
#---------------------------------------
# run = operations["*"]
# print(run(2,3))

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1,num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number ?: "))
calculation_function = operations[operation_symbol]
#second_answer = calculation_function(first_answer,num3)
second_answer = calculation_function(calculation_function(num1,num2),num3)

print(f"{num1} {operation_symbol} {num2} = {second_answer}")

#-----------------------------------------continue input from user untill No----------------

# Calculater

#Add 
def add(n1, n2):
    return n1 + n2

# Subtract
def subtract(n1 , n2):
    return n1 - n2

# Multiply
def multiply(n1 , n2):
    return n1 * n2

# Divide
def divide(n1 , n2):
    return n1 / n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

# function = operations["*"]
# function(2,3)
# print(function(2,3))
#print(function(2,3)= operations["*"])

num1 = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)
should_continue = True

while should_continue:

    operation_symbol = input("Pick an operation  ")
    num2 = int(input("what's the next number? "))

    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exirt. :" ) == "y":
        num1 = answer
    else:
        should_continue = False
# ---------------------------------------------Recursion-----------------------------------------
def caculator():
    print(logo)

    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation  ")
        num2 = int(input("what's the next number? "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}:") == "y":
            num1 = answer
        else:
            should_continue = False
            caculator()

caculator()

# def calculator():                      . Careful and Make sure that there is some sort of condition that needs to be met 
#     print("Raaj")                        in order for this function to call itself.   
#     calculator()
# calculator()


