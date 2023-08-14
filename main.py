import random
from turtle import Turtle, colormode, Screen

tim = Turtle()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


for _ in range(1000):
    tim.color(random_color())
    tim.speed("fastest")
    tim.circle(100)
    tim.setheading(tim.heading()+2)
tim.color("white")
screen = Screen()
screen.exitonclick()
