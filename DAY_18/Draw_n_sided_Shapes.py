from DAY_18 import my_turtle


def draw_shapes(num_sides):
    angle = 360 // num_sides
    for j in range(0, num_sides):
        my_turtle.forward(100)
        my_turtle.left(angle)


for i in range(3, 11):
    draw_shapes(i)
