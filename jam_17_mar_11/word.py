import sys
import numpy as np
from util import SolverBase


class WordSolver(SolverBase):

    def __call__(self):
        f_in = self._get_input_file()
        result = []
        for i, line in enumerate(f_in.readlines(), 1):
            grid_max, n = (int(p) for p in line.split(" "))
            gen = IOGenerator(grid_max, n)
            grid = gen.grid()
            result.append("Case #{}:\n{}".format(i, grid))
        f_in.close()
        self._write_result(result)


class IOGenerator(object):
    horizontal_pattern = "I/O"

    def __init__(self, grid_max, n):
        self.grid_max = grid_max
        self.n = n
        self.max_num_per_line = None
        if n != 0:
            self.max_num_per_line = int(np.floor(self.grid_max / 3))

    def grid(self):
        if self.n == 0:
            return "IO\n"
        elif self.n <= self.max_num_per_line:
            return self.horizontal_pattern * self.n + "\n"
        full_line = self.horizontal_pattern * self.max_num_per_line
        result = [full_line]
        n = self.n - self.max_num_per_line
        while n > 0:
            line_len = len(result[0])
            result.append("O"*line_len)
            if n >= self.max_num_per_line:
                result.append(full_line)
                n -= self.max_num_per_line
            else:
                line = self.horizontal_pattern * n
                line += 'O' * (line_len - len(line))
                result.append(line)
                break
            if len(result) == self.grid_max:
                raise ValueError("error")
        return "\n".join(result) + "\n"


if __name__ == "__main__":
    # python understudy.py C-small-practice
    WordSolver(sys.argv[1])()
