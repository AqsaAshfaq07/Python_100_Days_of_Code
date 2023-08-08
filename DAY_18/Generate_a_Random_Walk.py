from DAY_18 import my_turtle, screen
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def random_walk():
    my_turtle.color(random_color())
    direction = random.choice([90, 180, 270, 360])
    my_turtle.left(direction)
    my_turtle.forward(10)


for step in range(200):
    random_walk()

screen.exitonclick()
