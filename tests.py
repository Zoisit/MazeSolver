import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

        self.assertEqual(m1._cells[0][5]._y1, 0 + 5*10)
        self.assertEqual(m1._cells[0][5]._y2, 0 + 5*10 + 10)

        self.assertEqual(m1._cells[5][1]._x1, 0 + 5*10)
        self.assertEqual(m1._cells[5][1]._x2, 0 + 5*10 + 10)
        self.assertEqual(m1._cells[5][1]._y1, 0 + 1*10)
        self.assertEqual(m1._cells[5][1]._y2, 0 + 1*10 + 10)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 6
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 20, 10)
        
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[0][0].has_left_wall, True)
        self.assertEqual(m1._cells[0][0].has_bottom_wall, True)
        self.assertEqual(m1._cells[1][5].has_top_wall, True)
        self.assertEqual(m1._cells[3][2].has_bottom_wall, True)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)

        

if __name__ == "__main__":
    unittest.main()