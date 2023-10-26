import turtle


def rectangle(width, height):
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)


width = int(input())
height = int(input())
rectangle(width, height)