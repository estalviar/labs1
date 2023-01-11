from tkinter import *
from math import cos, sin

root = Tk()
root['bg'] = '#fafafa'
root.title('Анимация')

canvas = Canvas(root, width=600, height=600, bg="white")
canvas.pack()
xy_oval = 200
oval = canvas.create_oval(xy_oval, xy_oval, xy_oval + 200, xy_oval + 200, width=3)

xy_point, delta = 190, 100
point = canvas.create_oval(xy_point + delta, xy_point, xy_point + delta + 20, xy_point + 20, width=3, fill='green', outline='white')

parameters = [0, 0, 0]
data_speed = {
    '1': 50,
    '2': 10,
    '3': 1
}
data_direction = {
    '1': 1,
    '2': -1
}


def motion():
    radian = parameters[0] * (3.14 / 180) * data_direction[str(parameters[2])]
    a = cos(radian) * data_direction[str(parameters[2])]
    b = sin(radian) * data_direction[str(parameters[2])]
    parameters[0] += 0.578
    canvas.move(point, a, b)
    root.after(data_speed[str(parameters[1])], motion)


speed = int(input("Выберете скорость:\n1. Низкая скорость\n2. Средняя скорость\n3. Высокая скорость\n>> "))
direction = int(input("Выберете напраление:\n1. По часовой\n2. Против часовой\n>> "))

if not (1 <= speed <= 3) or not (1 <= direction <= 2):
    print("Были веденны некорректные данные!")
    exit(1)

parameters[1] = speed
parameters[2] = direction
motion()
root.mainloop()
