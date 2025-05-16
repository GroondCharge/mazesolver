from tkinter import Tk, BOTH, Canvas

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









def main():
    point1 = Point(0, 0)
    point2 = Point(800, 600)
    win = Window(800, 600)
    line = Line(point1, point2)
    win.draw_line(line, "red")
    win.wait_for_close()

main()

