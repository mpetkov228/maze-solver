from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 20, 20, 20, 20, win)
    maze._break_entrance_and_exit()

    win.wait_for_close()


main()