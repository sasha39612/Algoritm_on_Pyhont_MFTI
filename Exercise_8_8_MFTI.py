import turtle
turtle.shape("turtle")

def cantor_set_draw(l, n, x = 150, y = 150):
    if n == 0:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        return
    elif n >= 1:
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.forward(l)
        cantor_set_draw(l / 3, n - 1, x, y - 50)
        cantor_set_draw(l / 3, n - 1, x + (l / 3) * 2, y - 50)

cantor_set_draw(400, 5, x = - 400 / 2)

turtle.speed("fastest")
turtle.mainloop()