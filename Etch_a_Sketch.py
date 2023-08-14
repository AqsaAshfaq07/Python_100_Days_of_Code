from main import tim, screen


def move_forward():
    tim.setheading(0)
    tim.forward(10)


def move_up():
    tim.setheading(90)
    tim.forward(10)


def move_down():
    tim.setheading(-90)
    tim.forward(10)


def move_back():
    tim.setheading(0)
    tim.backward(10)


def turn_left():
    tim.setheading(tim.heading() - 10)
    tim.forward(10)


def turn_right():
    tim.setheading(tim.heading() + 10)
    tim.forward(10)


def clear_screen():
    tim.clear()
    tim.home()


screen.listen()
screen.onkey(key='space', fun=move_forward)
screen.onkey(key='Up', fun=move_up)
screen.onkey(key='Down', fun=move_down)
screen.onkey(key='BackSpace', fun=move_back)
screen.onkey(key='Right', fun=turn_left)
screen.onkey(key='Left', fun=turn_right)
screen.onkey(clear_screen, 'Home')

screen.exitonclick()