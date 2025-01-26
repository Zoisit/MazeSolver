from window import Window
from figures import Line, Point

class Cell():
    def __init__(self, x1:int, x2:int, y1:int, y2:int, win:Window, has_left_wall:bool=True, has_right_wall:bool=True, has_top_wall:bool=True, has_bottom_wall:bool=True):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        self.__x1, self.__x2, self.__y1, self.__y2 = x1, x2, y1, y2
        self.__win = win
        self.__color = "blue"

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2)), self.__color)
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1)), self.__color)
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2)), self.__color)
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2)), self.__color)