from graphics import Window, Line, Point


def main():
    line = Line(Point(3, 6), Point(500, 250))
    win = Window(800, 600)
    win.draw_line(line, "black")
    win.wait_for_close()


main()