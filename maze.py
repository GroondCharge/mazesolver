from grid import Cell, Window
from time import sleep
from random import seed

class Maze():
    def __init__(self, x1, y1,
                 num_rows, num_cols,
                 cell_size_x, cell_size_y,
                 win = None,
                 seed = None):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
    def _create_cells(self):
        print("number of rows" + str(self.num_rows))
        for i in range(self.num_rows):
            self._cells.append([])
            for j in range(self.num_cols):
                self._cells[i].append(Cell(self._win))
                if self._win:
                    self._draw_cell(j, i)
    def _draw_cell(self, i, j):
        if not self._win:
            return
        x1 = self._x1 + (i*self.cell_size_x)
        x2 = self._x1 + (i*self.cell_size_x) + self.cell_size_x
        y1 = self._y1 + (j*self.cell_size_y)
        y2 = self._y1 + (j*self.cell_size_y) + self.cell_size_y
        #cell= Cell(self._win)
        #cell.draw(x1, y1, x2, y2)
        self._cells[j][i].draw(x1, y1, x2, y2)
        self._animate()
    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        sleep(0.001)
            #print(self._cells[i])
        #for item in self._cells:
        #    print(item)
        #print(self._cells)
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[len(self._cells)-1][len(self._cells[len(self._cells)-1])-1].has_bottom_wall = False
        self._draw_cell(len(self._cells)-1, len(self._cells[len(self._cells)-1])-1)
#the_maze = Maze(0,0,4,4,10,10, Window(100,100))
#the_maze._create_cells()
