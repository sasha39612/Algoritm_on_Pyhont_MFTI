
from tkinter import *
def handler1(event):
    print('Hello, word! x=', event.x, 'y=', event.y)

def handler2(event):
    exit()

# инициализация
root = Tk()
hello_label = Label(root, text="Hello, Natasha!", font="Times 80")
hello_label.pack()

# привязка обработчиков - к паре (событие, виджету):
# виджет.bind(событие, обработчик)
hello_label.bind('<Button-1>', handler1)
hello_label.bind('<Button-3>', handler2)

# главный цикл (проект)

root.mainloop()