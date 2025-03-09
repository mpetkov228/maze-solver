import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells_1(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)


    def test_maze_create_cells_2(self):
        num_cols = 20
        num_rows = 12
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m._cells), num_cols)
        self.assertEqual(len(m._cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()