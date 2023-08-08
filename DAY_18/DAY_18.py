import turtle
from turtle import Turtle, Screen
import random

my_turtle = Turtle()
screen = Screen()

turtle.colormode(255)
my_turtle.shape('arrow')
my_turtle.color('magenta')
my_turtle.pensize(width=1)
my_turtle.speed("fastest")

# GUI
# Graphical User Interface

# TKInter
# A module which have a lot of colors described with their respective
# RGB values - Turtle relies on tkinter under the hood.

# Importing Modules
# 1- import ...  # Basic
# 2- from ... import ...
# 3- from .. import *
# 4- import ... as ...   # Aliasing

# Tuples
# A data structure to store data elements similar to an array
# Syntax -> my_tuple = (1, 2, 3)
# Immutable - values can't be changed
my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # generates an error of item assignment
print(my_tuple[0])

# Making the turtle stay on screen
screen.exitonclick()
