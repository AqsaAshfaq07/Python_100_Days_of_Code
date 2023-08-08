from DAY_18 import my_turtle, screen

for _ in range(50):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()

screen.exitonclick()