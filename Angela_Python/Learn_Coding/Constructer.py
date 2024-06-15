                                                # Python Constructors #

# constructor:- constructor is a special function that gets automatically calle when object of class created .
# Syntax to create constructor in python:-
# def __init__(self):       # self ek reference argument hain jo current object ko point out karta hai.
#           #code
# Note : The main purpose of constuctor is to create and initaize the object

# Types of constructor:- 1) Default Constructor 2) Parametrized Constructor

#  Default Constructor :- Are also called empty constructor , because it does'nt have any parameters.
# Note:- If we do not define any constructors ,the compiler automatically calls the default constructor.

# class A:
#     name = "Raaj"
#     age = 25
#     def __init__(self) -> None: # Automatically called 
#         address = "Ahmedabad"
#         print(self.name, " ", address)      # address is a local variable of this function show no need of self .
#     def Show_fun(self):         # We have to call this show_fun function
#         print(self.age)

# obj = A()
# obj.Show_fun()
#--------------------------------------------------------------------------------------------------------------------------
# Parametrized Constructor:- accept arguments along with self, it is known as parametrize constructor. 
# syntax:- class Class_Name:
#                 def __init__(self,1,2,3, ...):
#                             Code

class A:
    def __init__(self,age,name,addres):
        a = self.age
        b = self.name
        c = self.addres
        print(a,b,c)

obj = A(25,"Raaj","Ahmedabad")
        