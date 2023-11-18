import turtle
from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.pensize(15)
tim.speed("fastest")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple



directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

# coins = [1, -1]


# def random_move():
#     coin_flip = random.choice(coins)
#     direction = random.randint(1, 4)
#     if direction == 1:
#         tim.forward(50 * coin_flip)
#     elif direction == 2:
#         tim.backward(50 * coin_flip)
#     elif direction == 3:
#         tim.right(90)
#     else:
#         tim.left(90)
#
#
# for _ in range(100):
#     tim.color(random.choice(colors))
#     random_move()

screen = Screen()
screen.exitonclick()
