from os import path
import operator
from collections import defaultdict

JAM_DATA_DIR = path.join(path.dirname(__file__), "..", "data")


def get_local_data(name="C-sample"):
    filename1 = path.join(JAM_DATA_DIR, name + ".in")
    f = file(filename1, "r")
    n_sample = int(f.readline())
    data_input = [[int(s) for s in line.split(" ")] for line in f.readlines()]
    return data_input, name


def solve(data_input, name):
    out_file = file(path.join(JAM_DATA_DIR, name + ".out"), "w")
    for i, data in enumerate(data_input, 1):
        grid_max, n = data
        t_trouble = IOGenerator(grid_max, n)
        max_in_row = t_trouble.max_in_one_row()
        out_file.write("Case #{}: {}\n".format(i, max_in_row))
    out_file.close()


class IOGenerator(object):
    def __init__(self, grid_max, n):
        self.grid_max = grid_max
        self.n = n

    def grid(self):
        if self.n == 0:
            return "IO"
