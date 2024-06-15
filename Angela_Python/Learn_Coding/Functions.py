# If a group of statements is repeatedly required then it is not recommended to write these statements everytime seperately. 
# we have define these statements as a single unit and we can call that unit any number of times based on our requirement without rewriting.
# This unit is notjhing but function.
# Function is nothing but group of statements which only execute when we call the function.
# Note:-    1) Code Reusability
#           2) Functions returns value as a result.
#           3) We can pass value to the functions called parameters.
# Types 1) Pre-defined / Built-in function: (which comes with python)
#           e.g len(),print(), int() etc..    
#       2) User-defined function: (we create to fullfill our business requirement)
# Types of function arguments:
# 1) Positional : Order should be maintained and No. of parameter = No. of arguments
# 2) Keyword arguments : order is not important and No. of parameter = No. of arguments
# Note:- keyword arguments should follow positional arguments.
# Keyword arguments hamesha last main hona chahiye pehle nahi with positional arguments
# 3) Default arguments: 1) Order is important 2) no.of parameter may or may not be equal no. of arguments
# 4) variable length arguments: take any number of variable length arguments take
#       1) *args    2) **kwrgs :- for key value pair data
#Syntax:_) 


# def function_name():
#     print("Good morning")

# function_name() # calling function
# msg = function_name()
# print(msg)

# def great():
#     return "Good Morning"
# obj = great()
# print(obj)

# # Positional arguments
# def great(first_name,Last_name):
#     print("Good Mornig",first_name,Last_name)
# great("Raaj","Kumar")

# # Key word arguments
# def great(first_name,Last_name):
#     print("Good Mornig",first_name,Last_name)
# great(first_name="Aparna",Last_name="Ray")

# Default argument
def test(*args):
    print("Good morning")
    print(args)
    print(len(args))
    print(type(args))

test()
test("India", "America", "Srilanka")

# Default argument (**kwrgs)
def test(**kwrgs):
    print("Good morning")
    print(kwrgs)
    print(len(kwrgs))
    print(type(kwrgs))

test()
test(India="delhi", America="washington", Srilanka="colombo")


