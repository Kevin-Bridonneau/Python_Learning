import turtle

t = turtle.Turtle()


def escalier(width, nb):
    for i in range(0, nb):
        t.forward(width)
        t.left(90)
        t.forward(width)
        t.right(90)
    t.forward(width)


def square(width):
    for i in range(0, 4):
        t.forward(width)
        t.left(90)


def squares(width, nb):
    for i in range(0, nb):
        square((i+1)*width)

# escalier(50,4)


squares(20, 12)


turtle.done()
