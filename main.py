#from tkinter import Tk, BOTH, Canvas
from grid import Window, Point, Line, Cell
from maze import Maze
def main():
    #point1 = Point(0, 0)
    #point2 = Point(800, 600)
    win = Window(640, 640)
    #line = Line(point1, point2)
    #win.draw_line(line, "red")
    #win.wait_for_close()
    #celica1 = Cell(win)
    #celica1.draw(100, 100, 110, 110)
    #celica2 = Cell(win)
    #celica2.draw(200, 200, 210, 210)
    #celica1.draw_move(celica2, True)
    the_maze = Maze(20, 20, 30, 30, 20, 20, win)
    win.wait_for_close()
main()

