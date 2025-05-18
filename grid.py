from tkinter import Tk, BOTH, Canvas
#from window import Line, Point, Window

class Window():
    def __init__(self, width, height):
        self.root= Tk()
        self.root.minsize(width, height)
        self.root.maxsize(width, height)
        self.root.title("testni naslov")
        self.widget = Canvas(self.root, bg = "gray", height = height, width = width)
        self.widget.pack(fill = BOTH, expand = 1)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.widget.update_idletasks()
        self.widget.update()
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
        print("window closed")
    def close(self):
        self.running = False
    def draw_line(self, line, fill_color):
        line.draw(self.widget,  fill_color)



class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(
                self.point1.x, self.point1.y,
                self.point2.x, self.point2.y,
                fill = fill_color, width = 2
                )


class Cell():
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = False
        self.has_bottom_wall = False
        
        self.width = 5


        self._x1 = -1
        self._x2 = -1
        self._y1 = -1
        self._y2 = -1

        self._win = window

    def draw(self, x, y):
        self._x1 = x - self.width
        self._y1 = y + self.width
        self._x2 = x + self.width
        self._y2 = y - self.width
        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), "red")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), "red")
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), "red")
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), "red")

