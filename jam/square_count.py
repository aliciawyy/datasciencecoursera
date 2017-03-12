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
        n_square = (length - 1) * (width - 1)
        if width == 2:
            return n_square
        # Count regular square
        for sq_edge in range(2, width):
            n_square += (length - sq_edge) * (width - sq_edge)
        # Count not straight square
        for sq_edge_left in range(1, width - 1):
            for sq_edge_right in range(1, width - sq_edge_left):
                n_length = length - sq_edge_left - sq_edge_right
                n_width = width - sq_edge_left - sq_edge_right
                n_square += n_length * n_width
                n_square = n_square % self.threshold
        return n_square


if __name__ == "__main__":
    import sys
    # python -m jam.square_count B-large-practice
    SquareCountSolver(sys.argv[1])()
