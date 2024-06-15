class User:
    pass
user_1 = User()

def function():
    pass
print("Jack")
#-----------------------------------------------------------------------------------------------------------------------------
# Working with Attributes,class constructers & the --init--()
class User:
    def __init__(self, user_id,username):
        self.id = user_id       # Different names , you can name either of these anything you want
        self.username = username # its normally convention that you will see that name of the parameter be equal to the name of the attributes.
        self.followers = 0

# user_1 = User()
# user_1.id = "001"
# user_1.username = "Raaj"
user_1 = User("003", "Aparna")

print(user_1.username)
print(user_1.id)
print(user_1.followers)


# user_2 = User() # Remember when you add parameter to the constructor which is init function , must provide pieces of data.
# user_2.id = "002"
# user_2.name = "Angela"
#
# print(user_2.name)


# Attribute
class Car:
    def __init__(self, seats): # You can add as many as parameter as you wish. And that parameter is going  to be passed in when an object gets constructed from the class
        self.seats = seats

# Crete Constructer is by using a special function [ init function ]
# When our object is being constructed and this is also known as initializing an object 

class Car:
    def __init__(self) -> None:
        pass
    # initialise attributes

# Final conclusion
class User:
    def __init__(self, user_id,username):
        self.id = user_id       # Different names , you can name either of these anything you want
        self.username = username # its normally convention that you will see that name of the parameter be equal to the name of the attributes.
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1

user_1 = User("001", "Aparna")
user_2 = User("002", "Raaj")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

