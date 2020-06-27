import turtle
turtle.shape("turtle")

def dragon_draw(l, n, angle = 45):
    if n:
        turtle.right(angle)
        dragon_draw(l, n - 1, 45)
        turtle.left(angle * 2)
        dragon_draw(l, n - 1, -45)
        turtle.right(angle)
    else:
        turtle.forward(l)

dragon_draw(50, 2)

turtle.speed("fastest")
turtle.mainloop()

if __name__ == '__main__': main()