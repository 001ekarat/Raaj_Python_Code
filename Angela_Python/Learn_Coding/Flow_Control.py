# Flow control describes the order in which statements will be executed at runtime.
# Conditialnal statement:- if, if else, else if 
# Syntax:-01
# if condition:
#     statement
#-----------------------------------02
# if condition:
#     statement
# else:
#     statement
#-----------------------------------03
# if condition:
#     statement
# elif condition:
# else:
#     statement

user_input = int(input("enter a number : "))

if user_input % 2 == 0:
    print("number is even")

age = int(input("enter your age  : "))

if age < 18:
    print("You are too young to marry")
elif 60 > age > 40:
    print("Dhundhna padega")

else:
    print("We will find a perfect match for you ")