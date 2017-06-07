from tkinter import *
from parameters import WIN_SIZE


root = Tk()
can = Canvas(root, width=WIN_SIZE, height=WIN_SIZE)
can.pack()


def _create_circle(self, x, y, r, **kwargs):
    # Builds higher level function to draw circle
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


def _draw_point(self, point):
    # Builds higher level function to draw our points
    return self.create_circle(point.x, point.y, 1, fill=point.color, outline="")
Canvas.draw_point = _draw_point


def draw_point(point):
    can.draw_point(point)
