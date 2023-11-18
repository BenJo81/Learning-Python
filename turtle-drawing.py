from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("DarkGreen")

colors = ["deep sky blue", "lawn green", "magenta", "yellow", "navy", "dark slate gray",
          "dark khaki", "light coral", "medium purple"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
