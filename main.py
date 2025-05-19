#from tkinter import Tk, BOTH, Canvas
from grid import Window, Point, Line, Cell

def main():
    point1 = Point(0, 0)
    point2 = Point(800, 600)
    win = Window(800, 600)
    line = Line(point1, point2)
    win.draw_line(line, "red")
    #win.wait_for_close()
    celica1 = Cell(win)
    celica1.draw(399, 499)
    celica2 = Cell(win)
    celica2.draw(699, 200)
    celica1.draw_move(celica2, True)
    win.wait_for_close()
main()

