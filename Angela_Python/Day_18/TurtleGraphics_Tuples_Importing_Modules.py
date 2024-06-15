# import turtle  , The reason is because turtle is a module that is packaged with the Python standard library
#tim = turtle.Turtle()
# Aliasing Modules 
#import turtle as t [some time module name is really long name and you don't want to type it out every single time.]
#tim = t.Turtle()

from turtle import Turtle, Screen

tim = Turtle()
tim.shape("triangle")
tim.shape("turtle")
tim.color("red", "green")

for _ in range(4):
    tim.fd(100)
    tim.lt(90)








tim.screen.title('Object-oriented turtle demo')
tim.screen.bgcolor("orange")
Screen = Screen()
Screen.exitonclick()

# Installing Modules
import heroes # ModuleNotFoundError: No module named 'heroes' becuase not come with python . 
# Python packages which hosted on the internet which are not come with python  .