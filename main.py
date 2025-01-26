from window import Window
from figures import Point, Line
from maze import Cell

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(200, 200), Point(400, 400)), "red")
    win.draw_line(Line(Point(300, 600), Point(500, 100)), "blue")
    win.draw_line(Line(Point(30, 10), Point(800, 600)), "green")
    cell1 = Cell(0, 100, 0, 100, win)
    cell1.draw()
    cell2 = Cell(150, 250, 0, 100, win)
    cell2.draw()
    cell3 = Cell(150, 350, 300, 150, win, has_left_wall=False)
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)
    win.wait_for_close()

main()