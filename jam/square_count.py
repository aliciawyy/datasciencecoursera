"""
http://code.google.com/codejam/contest/8284486/dashboard
"""
from .util import (SolverBase, sum_of_int_cube, sum_of_int_square,
                   sum_of_int)


class SquareCountSolver(SolverBase):
    def __call__(self):
        result = []
        for line in self._iter_input():
            n_dots, n_col = self._split_line_to_list(line)
            grid = DotGrid(n_dots, n_col)
            result.append(grid())
        self._write_result(result)


class DotGrid:
    threshold = 1000000007

    def __init__(self, n_dots, n_col):
        self.n_row = n_dots
        self.n_col = n_col

    def __call__(self):
        # sum[(r-k)*(c-k)*k], 1  <= k <= min(r, c)
        n = min(self.n_row, self.n_col)
        n_square = sum_of_int_cube(n, self.threshold)
        square_sum = sum_of_int_square(n, self.threshold)
        n_square -= self._mod((self.n_row + self.n_col) * square_sum)
        n_square += self.n_row * self.n_col * sum_of_int(n, self.threshold)
        return self._mod(n_square)

    def _mod(self, x):
        return x % self.threshold


if __name__ == "__main__":
    import sys
    # python -m jam.square_count A-large-practice
    SquareCountSolver(sys.argv[1])()
