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


    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        top_left_cell = m._cells[0][0]
        bottom_right_cell = m._cells[num_cols-1][num_rows-1]
        self.assertFalse(top_left_cell.has_top_wall)
        self.assertFalse(bottom_right_cell.has_bottom_wall)

    
    def test_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m._cells:
            for cell in col:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()