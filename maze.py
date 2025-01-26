from window import Window
from figures import Line, Point
import time

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

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
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

    def _draw_cell(self, cell):       
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
