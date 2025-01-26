from window import Window
from figures import Point, Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(200, 200), Point(400, 400)), "red")
    win.draw_line(Line(Point(300, 600), Point(500, 100)), "blue")
    win.draw_line(Line(Point(30, 10), Point(800, 600)), "green")
    win.wait_for_close()

main()