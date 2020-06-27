
import graphics as gr
''' не перемещает шарик по орбите, только движеие прямо'''


SIZE_X = 800
SIZE_Y = 800
x = 0
y = 0

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
circle = gr.Circle(gr.Point(400, 400), 10)
circle.setFill('red')
circle.draw(window)

coords = gr.Point(400, 700) # начальное положеие шарика
#velocity = gr.Point(2, 0)   # скорость
acceleration = gr.Point(0, 0) # гравитация

def add(point_1, point_2):
    new_point = gr.Point(point_1.x + point_2.x,
                         point_1.y + point_2.y)
    return new_point

def sub (point_1, point_2):
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    return new_point

#def clear_window():                                                     # очистка экрана
#    recangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
 #   recangle.setFill('cyan')
  #  recangle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)             # Солнце
sun.setFill('yellow')
sun.draw(window)


#def drow_ball(coords):                  # отрисовка шарика
#circle = gr.Circle(coords, 10)
#circle = gr.Circle(gr.Point(400, 400), 10)
    #circle.setFill('red')

    #circle.draw(window)

#def check_cords(coords, velocit):                       # отражение от баръера (стены)
#    if coords.x < 0 or coords.x > SIZE_X:
#        velocit.x = - velocit.x
#    if coords.y < 0 or coords.y > SIZE_Y:
#        velocit.y = - velocit.y

#def update_coords(coords, velocity):
#    return add(coords, velocity)

#def update_velocity(velocity, acceleration):                        # пересчет гравитации
#    return add(velocity, acceleration)

def update_acceleration(ball_coords, center_coords):                # изменение ускорения в каждый момент времени
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3/2)

    G = 2000

    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2)


while True:

#    clear_window()
#    drow_ball(coords)
    circle.move(x, y)

    acceleration = update_acceleration(coords, gr.Point(400, 400))
#    coords = update_coords(coords, velocity)
#    velocity = update_velocity(velocity, acceleration)
#    check_cords(coords, velocity)
    gr.time.sleep(0.02)
