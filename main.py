from graphics import Window, Line, Point
from maze import Maze
from cell import Cell


def main():
    win = Window(800, 600)

    # c1 = Cell(win)
    # c1.has_left_wall = False
    # c1.draw(50, 50, 100, 100)

    # c2 = Cell(win)
    # c2.has_right_wall = False
    # c2.draw(125, 125, 200, 200)

    # c1.draw_move(c2, True)

    maze = Maze(50, 50, 20, 20, 10, 10, win)


    win.wait_for_close()


main()