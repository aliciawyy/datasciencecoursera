from os import path
import operator
from collections import defaultdict

JAM_DATA_DIR = path.join(path.dirname(__file__), "..", "data")


def get_input():
    # raw_input() reads a string with a line of input,
    # stripping the '\n' (newline) at the end.
    # This is all you need for most Google Code Jam problems.
    n_sample = int(raw_input())  # read a line with a single integer
    data_input = [[int(s) for s in line.split(" ")] for line in raw_input()]
    return data_input, n_sample


def get_local_data(name="A-small-practice"):
    filename1 = path.join(JAM_DATA_DIR, name + ".in")
    f = file(filename1, "r")
    n_sample = int(f.readline())
    data_input = [[int(s) for s in line.split(" ")] for line in f.readlines()]
    return data_input, n_sample


def solve(data_input, n_sample):
    current_ind = 0
    out_file = file(path.join(JAM_DATA_DIR, "tt-large.out"), "w")
    for i in xrange(1, n_sample + 1):
        n_friends, n_grid = data_input[current_ind]
        end = current_ind + n_friends + 1
        tickets = data_input[current_ind + 1:end]
        t_trouble = TicketTrouble(n_grid, tickets)
        max_in_row = t_trouble.max_in_one_row()
        out_file.write("Case #{}: {}\n".format(i, max_in_row))
        current_ind = end
    out_file.close()


class TicketTrouble(object):
    def __init__(self, n_grid, tickets):
        self.n_grid = n_grid
        self.tickets = tickets

    def max_in_one_row(self):
        result = defaultdict(int)
        seats = set()
        for seat in self.tickets:
            seat = tuple(seat)
            if seat in seats:
                continue
            seats.add(seat)
            row, col = seat
            result[row] += 1
            if col != row:
                result[col] += 1
        return max(result.iteritems(), key=operator.itemgetter(1))[1]
