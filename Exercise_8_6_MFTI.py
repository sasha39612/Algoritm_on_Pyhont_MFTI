import turtle
turtle.shape("turtle")

def levi_draw(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        turtle.left(45)
        levi_draw(l / 2, n - 1)
        turtle.right(90)
        levi_draw(l / 2, n - 1)
        turtle.left(45)

levi_draw(1900, 9)

turtle.speed("fastest")
turtle.mainloop()