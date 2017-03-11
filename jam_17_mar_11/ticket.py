import sys
from os import path
import operator
from collections import defaultdict


class TicketSolver:
    DATA_DIR = path.join(path.dirname(__file__), "..", "data", "ticket")

    def __init__(self, name):
        self.name = name

    def __call__(self):
        data_input, n_sample = self.get_local_data()
        current_ind = 0
        out_file = self._get_file_handler('out')
        for i in xrange(1, n_sample + 1):
            n_friends, n_grid = data_input[current_ind]
            end = current_ind + n_friends + 1
            tickets = data_input[current_ind + 1:end]
            t_trouble = TicketTrouble(n_grid, tickets)
            max_in_row = t_trouble.max_in_one_row()
            out_file.write("Case #{}: {}\n".format(i, max_in_row))
            current_ind = end
        out_file.close()

    def _get_file_handler(self, ext):
        op = 'r' if ext == 'in' else 'w'
        return file(path.join(self.DATA_DIR, self.name + "." + ext), op)

    def get_local_data(self):
        f = self._get_file_handler('in')
        n_sample = int(f.readline())
        data_input = [[int(s) for s in line.split(" ")]
                      for line in f.readlines()]
        return data_input, n_sample


class TicketTrouble:
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


if __name__ == '__main__':
    TicketSolver(sys.argv[1])()
