from window import Window
from figures import Line, Point
import time
import random

class Cell():
    def __init__(self, x1:int, x2:int, y1:int, y2:int, win:Window=None, has_left_wall:bool=True, has_right_wall:bool=True, has_top_wall:bool=True, has_bottom_wall:bool=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        self._x1, self._x2, self._y1, self._y2 = x1, x2, y1, y2
        self._win = win
        self._color = "blue"
        self._visited = False

    def draw(self):
        #if self.has_left_wall:
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), self._color if self.has_left_wall else "white")
        #if self.has_top_wall:
        self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), self._color if self.has_top_wall else "white")
        #if self.has_right_wall:
        self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), self._color if self.has_right_wall else "white")
       # if self.has_bottom_wall:
        self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), self._color if self.has_bottom_wall else "white")

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        point1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
        point2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)

        if point1.x > point2.x or (point1.x == point2.x and point1.y > point2.y):
            point1, point2 = point2, point1

        line = Line(point1, point2)
        self._win.draw_line(line, color)

    def get_middle_point(self) -> Point:
        return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win:Window = win

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

        if seed is not None:
            random.seed(seed)

    def _create_cells(self):
        self._cells = []
        for c in range(self._num_cols):
            cur_col = []
            for r in range(self._num_rows):
                x1 = self._x1 + c * self._cell_size_x
                x2 = self._x1 + self._cell_size_x + c * self._cell_size_x
                y1 = self._y1 + r * self._cell_size_y
                y2 = self._y1 + self._cell_size_y + r * self._cell_size_y

                cell = Cell(x1, x2, y1, y2, self._win)

                cur_col.append(cell)
                self._draw_cell(cell)
            self._cells.append(cur_col)

    def _draw_cell(self, cell:Cell):       
        if self._win is not None:
            cell.draw()
            self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(self._cells[0][0])
        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(self._cells[-1][-1])

    def _break_walls(self, c1, r1, c2, r2):
        #right = c + 1
        if c2 > c1:
            self._cells[c1][r1].has_right_wall = False
            self._draw_cell(self._cells[c1][r1])
            self._cells[c2][r2].has_left_wall = False
            self._draw_cell(self._cells[c2][r2])
        #left = c - 1
        elif c2 < c1:
            self._cells[c1][r1].has_left_wall = False
            self._draw_cell(self._cells[c1][r1])
            self._cells[c2][r2].has_right_wall = False
            self._draw_cell(self._cells[c2][r2])
        #top = r - 1
        elif r2 < r1:
            self._cells[c1][r1].has_top_wall = False
            self._draw_cell(self._cells[c1][r1])
            self._cells[c2][r2].has_bottom_wall = False
            self._draw_cell(self._cells[c2][r2])
        #bottom = r + 1
        elif r2 > r1:
            self._cells[c1][r1].has_bottom_wall = False
            self._draw_cell(self._cells[c1][r1])
            self._cells[c2][r2].has_top_wall = False
            self._draw_cell(self._cells[c2][r2])

    def _break_walls_r(self, c, r):
        self._cells[c][r]._visited = True

        while True:
            to_visit = []

            # potential neighbors:
            right = c + 1
            left = c - 1
            top = r - 1
            bottom = r + 1
            if right < self._num_cols and not self._cells[right][r]._visited:
                to_visit.append((right, r))
            if left > 0 and not self._cells[left][r]._visited:
                to_visit.append((left, r))
            if bottom < self._num_rows and not self._cells[c][bottom]._visited:
                to_visit.append((c, bottom))
            if top > 0 and not self._cells[c][top]._visited:
                to_visit.append((c, top))

            if len(to_visit) == 0:
                self._draw_cell(self._cells[c][r])
                return
            
            next = random.randint(0, len(to_visit)-1)
            self._break_walls(c, r, to_visit[next][0], to_visit[next][1])
            self._break_walls_r(to_visit[next][0], to_visit[next][1])

    def _reset_cells_visited(self):
        for c in range(self._num_cols):
            for r in range(self._num_rows):
                self._cells[c][r]._visited = False

    def _solve_r(self, c, r):
        
        self._animate()
        self._cells[c][r]._visited = True

        if c == self._num_cols - 1 and r == self._num_rows -1:
            return True
        
        middle_point =  self._cells[c][r].get_middle_point()

        # potential neighbors:
        to_visit = []
        if c + 1 < self._num_cols and not self._cells[c + 1][r]._visited and not self._cells[c][r].has_right_wall:
            to_visit.append((c + 1, r))
        
        if r + 1 < self._num_rows and not self._cells[c][r + 1]._visited and not self._cells[c][r].has_bottom_wall:
            to_visit.append((c, r + 1))
        left = c - 1
        if left > 0 and not self._cells[left][r]._visited and not self._cells[c][r].has_left_wall:
            to_visit.append((left, r))
        top = r - 1
        if top > 0 and not self._cells[c][top]._visited and not self._cells[c][r].has_top_wall:
            to_visit.append((c, top))
        
        

        for neighbor in to_visit:
            self._win.draw_line(Line(middle_point, self._cells[neighbor[0]][neighbor[1]].get_middle_point()), "orange")
            result = self._solve_r(neighbor[0], neighbor[1])
            if result:
                return result
            else:
                self._win.draw_line(Line(middle_point, self._cells[neighbor[0]][neighbor[1]].get_middle_point()), "white")

        return False

    def solve(self):
        self._solve_r(0, 0)

