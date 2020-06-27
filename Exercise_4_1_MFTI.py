
import graphics as gr

window = gr.GraphWin("Russian game", 500, 500)

def draw_backgounr():
    background = gr.Rectangle(gr.Point(0, 0), gr.Point(500, 250))
    background1 = gr.Rectangle(gr.Point(0, 250), gr.Point(500, 500))

    background.setFill("blue")
    background1.setFill("grey")

    background.draw(window)
    background1.draw(window)

def draw_house():
    house = gr.Rectangle(gr.Point(200, 350), gr.Point(350, 200))
    roof = gr.Polygon(gr.Point(200, 200), gr.Point(350, 200), gr.Point(275, 120))

    house.setFill("cyan")
    roof.setFill("red")

    house.draw(window)
    roof.draw(window)

def draw_windows():
    windows = gr.Rectangle(gr.Point(250, 300), gr.Point(300, 250))
    windows1 = gr.Line(gr.Point(275, 300), gr.Point(275, 250))
    windows2 = gr.Line(gr.Point(250, 275), gr.Point(300, 275))

    windows.setFill('yellow')
    windows1.setFill("black")
    windows2.setFill("black")

    windows.draw(window)
    windows1.draw(window)
    windows2.draw(window)


def draw_clouds(x, y, size):
    clouds = gr.Circle(gr.Point(x+10, y), size)
    clouds1 = gr.Circle(gr.Point(x+30, y), size)
    clouds2 = gr.Circle(gr.Point(x, y+30), size)
    clouds3 = gr.Circle(gr.Point(x+40, y+30), size)
    clouds4 = gr.Circle(gr.Point(x+60, y+30), size)
    clouds5 = gr.Circle(gr.Point(x+20, y+40), size)
    clouds6 = gr.Circle(gr.Point(x+40, y+50), size)


    clouds.setFill("white")
    clouds1.setFill("white")
    clouds2.setFill("white")
    clouds3.setFill("white")
    clouds4.setFill("white")
    clouds5.setFill("white")
    clouds6.setFill("white")

    clouds.draw(window)
    clouds1.draw(window)
    clouds2.draw(window)
    clouds3.draw(window)
    clouds4.draw(window)
    clouds5.draw(window)
    clouds6.draw(window)

def draw_sun(x, y, size):
    sun = gr.Circle(gr.Point(x, y), size)

    sun.setFill("yellow")

    sun.draw(window)

def draw_landscape():
    draw_backgounr()
    draw_clouds(100, 50, 25)
    draw_sun(400, 100, 40)
    draw_house()
    draw_windows()

draw_landscape()

window.getMouse()
window.close()