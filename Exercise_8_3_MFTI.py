
import turtle
turtle.shape('turtle')

def draw(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        draw(l / 3, n - 1)
        turtle.left(60)
        draw(l / 3, n - 1)
        turtle.right(120)
        draw(l / 3, n - 1)
        turtle.left(60)
        draw(l / 3, n - 1)

    turtle.speed('fastest')

draw(600, 4)

#turtle.mainloop()
