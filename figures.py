from tkinter import Canvas

class Point():
    def __init__(self, x, y):
        self.x = x #x=0 -> left
        self.y = y #y=0 -> top

class Line():
    def __init__(self, point1:Point, point2:Point):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas:Canvas, fill_color:str):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )