from grid import Cell, Window
from time import sleep
import random

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
        
        random.seed(seed)
        self._win = win
        
        self._seed = 0
        self._cells = []
        self._create_cells()
        self._break_walls_r(0,0)
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
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[len(self._cells)-1][len(self._cells[len(self._cells)-1])-1].has_bottom_wall = False
        self._draw_cell(len(self._cells)-1, len(self._cells[len(self._cells)-1])-1)
    def _check_adjacent(self, i, j):
        adjacent = []
        if i-1 >= 0:
            if not self._cells[i-1][j].visited:
                adjacent.append((i-1, j))
        if i+1 <= len(self._cells) -1:
            if not self._cells[i+1][j].visited:
                adjacent.append((i+1, j))
        if j-1 >= 0:
            if not self._cells[i][j-1].visited:
                adjacent.append((i, j-1))
        if j+1 <= len(self._cells[i]) -1:
            if not self._cells[i][j+1].visited:
                adjacent.append((i, j+1))
        return adjacent
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            future_visits = []
            #if self._check_adjacent(i, j):
            future_visits.extend(self._check_adjacent(i, j))
            if not future_visits:
                self._draw_cell(i, j)
                return
            #chosen_direction = random.choice(future_visits)
            chosen_direction = future_visits.pop(random.randrange(len(future_visits)))
            print(chosen_direction)
            print(self._cells[i][j])
            if i != chosen_direction[0]:
                if i > chosen_direction[0]:
                    self._cells[i][j].has_top_wall = False
                    self._cells[chosen_direction[0]][j].has_bottom_wall = False
                else: 
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[chosen_direction[0]][j].has_top_wall = False
            if j != chosen_direction[1]:
                if j > chosen_direction[1]:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][chosen_direction[1]].has_right_wall = False
                else:
                    print(self._cells[i][j].has_right_wall)
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][chosen_direction[1]].has_left_wall = False
            self._break_walls_r(chosen_direction[0], chosen_direction[1])
                    
                    
            
            
            
#the_maze = Maze(0,0,4,4,10,10, Window(100,100))
#the_maze._create_cells()
