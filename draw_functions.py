from tkinter import *


def _create_circle(self, x, y, r, **kwargs):
    # Builds higher level function to draw circle
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.create_circle = _create_circle


def _draw_point(self, point):
    # Builds higher level function to draw our points
    return self.create_circle(point.x, point.y, 1, fill=point.color, outline="")
Canvas.draw_point = _draw_point
