import turtle
turtle.shape("turtle")

def minkovskogo_draw(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        minkovskogo_draw(l / 8, n - 1)
        turtle.left(90)
        minkovskogo_draw(l / 8, n - 1)
        turtle.right(90)
        minkovskogo_draw(l / 8, n - 1)
        turtle.right(90)
        minkovskogo_draw(l / 4, n - 1)
        turtle.left(90)
        minkovskogo_draw(l / 8, n - 1)
        turtle.left(90)
        minkovskogo_draw(l / 8, n - 1)
        turtle.right(90)
        minkovskogo_draw(l / 8, n - 1)

minkovskogo_draw(100, 1)

turtle.speed('fastest')
turtle.mainloop()