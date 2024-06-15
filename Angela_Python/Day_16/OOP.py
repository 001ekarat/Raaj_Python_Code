# Object Oriented Programming (OOP)

# Procedural Programming
# How to use OOP
#-----------------------------------------------------------
# Creating an objrct from a blueprint that somebody else has already created,
from turtle import Turtle, Screen # instead this import turtle

timmy = Turtle() # timmy = turtle.Turtle()

print(timmy)
timmy.shape("turtle")
timmy.color("coral")

my_screen = Screen()
print(my_screen.canvheight) # Screen is the object and that canvas height is an attribute
print(Screen().canvheight)

my_screen.exitonclick()
