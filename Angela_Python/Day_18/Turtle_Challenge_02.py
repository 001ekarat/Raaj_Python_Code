# Draw a Dashed Line
import turtle as t
tim = t.Turtle()
import random


# for _ in range(15):

#     tim.fd(10)
#     tim.penup()
#     tim.fd(10)
#     tim.pendown()
#num_sides = 5
colorList = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink', 'brown', 'gray', 'gold']

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        angle = 360/num_sides
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3,11):
    tim.color(random.choice(colorList))
    draw_shape(shape_side_n)


