from turtle import Turtle
from turtle import Screen
import random

tim = Turtle()
tim.pensize(15)
tim.speed("fastest")

colors = ["deep sky blue", "lawn green", "magenta", "yellow", "navy", "dark slate gray",
          "dark khaki", "light coral", "medium purple", "tomato"]
directions = [0, 90, 180, 270]


for _ in range(200):
    tim.color(random.choice(colors))
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
