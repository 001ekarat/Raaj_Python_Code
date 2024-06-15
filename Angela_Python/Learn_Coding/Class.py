# Class:- class is a blueprint for an object. like - Real world entity has some properties or behaviour which is represented by class variables & methods in programming.
# Syntax:_ class Class_Name:
#                   Variable
#                   Methods         # Class is just a template does't take memory, if we have to use variable and methods then w have to create " Ojects "
#   Object:- As we know class is a logical entity while an object is a physical or real entity that works on classes data.
#   Note:- Each Object has a distinct role or responibility
#          Object creates space on memory as per class members.
#   Syntax:- obj_name = Class_Name()

# class Class_Name:
#     pass
# object_1 = Class_Name()
# object_2 = Class_Name()
# object_3 = Class_Name()
# print(id(object_1))
# print(id(object_2))
# print(id(object_3))

# class A:
#     a = 10
#     print("Good Evening")
#     print(a)
#-------------------------------------------------------------------------------------------------------------------------------
# class A:
#     def __init__(self):                  
#         a = 10
#         print("Good Evening")   # No output print because constructer is a class member and for class member call object is necessary requarement .
#         print(a)                # "Self" is a default reference parameter which represent current object.
#--------------------------------------------------------------------------------------------------------------------------------
# class A:
#     "Thinking about Aparna "  # if any string is written in class then it most be written in first line of code.
#     a = 10
#     print("Good Evening")
#     print(a)

#-------------------------------------------------------------------------------------------------------------------------------
# obj = A()
# print(obj.__doc__)
# print(A.a)              # class k variable ko hum class k object aur class k name se bhi access kar shakte hai.
# print(obj.a)

#-------------------------------------------------------------------------------------------------------------------------------
# class A:                                     qaury raised
#     age=10
#     def fun(self):
#         "Great Nilesh "
#         name = "Keybourd"
#         variable = 15
#         print(name)

# obj = A()
# obj.fun()
# print(obj.fun.__doc__)
# pass
# print(obj.fun.name)
# pass
# print(obj.fun.variable)
# print(obj.age)
# print(A.age)
#------------------------------------------------------------------------------------------------------------------------------
class A:
    def __init__(self):
        pass

    def fun(self,  name, mobile , address):
        print(f"name is {name} mobile No is {mobile} and address is {address}")

obj = A()
obj.fun("nilesh",16461545,"ahmedabad")
        