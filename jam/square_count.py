from .util import SolverBase


class SquareCountSolver(SolverBase):
    def __call__(self):
        result = []
        for line in self._iter_input():
            n_dots, n_col = self._split_line_to_list(line)
            grid = DotGrid(n_dots, n_col)
            result.append(grid.count())
        self._write_result(result)


class DotGrid:
    threshold = 1000000007

    def __init__(self, n_dots, n_col):
        self.n_dots = n_dots
        self.n_col = n_col

    def count(self):
        width = min(self.n_dots, self.n_col)
        length = max(self.n_dots, self.n_col)
        diff = (length - width) % self.threshold
        n_square = 0
        # Count regular square
        for n_width in range(1, width):
            n_square += (n_width + diff) * n_width
            n_square = n_square % self.threshold
        # Count not straight square
        for n_width in range(2, width):
            for n_width0 in range(1, n_width):
                n_length = diff + n_width0
                n_square += n_length * n_width0
                n_square = n_square % self.threshold
        return n_square


if __name__ == "__main__":
    import sys
    # python -m jam.square_count B-large-practice
    SquareCountSolver(sys.argv[1])()
