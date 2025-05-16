from tkinter import Tk, BOTH, Canvas
from window import Line, Point


class Cell():
    def __init__(self, poin1, point2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = point1.x
        self._x2 = point2.x
        self._y1 = point1.y
        self._y2 = point2.y
        
        self._win = False

    def draw(self, canvas, fill_color):
        if self.has_left_wall:
            canvas.create_line(
                    self.point1.x, self.point1.y,
                    self.point1.x, self.point2.y,
                    fill = fill_color,width = 2
                    )
        if self.has_right_wall:
            canvas.create_line(
            
                    )

