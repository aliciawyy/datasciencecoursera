import sys
import operator
from collections import defaultdict


from .util import SolverBase


class TicketSolver(SolverBase):

    def __call__(self):
        data_input = self.get_local_data()
        current_ind = 0
        result = []
        for i in range(self.n_sample_):
            n_friends, n_grid = data_input[current_ind]
            end = current_ind + n_friends + 1
            tickets = data_input[current_ind + 1:end]
            t_trouble = TicketTrouble(n_grid, tickets)
            max_in_row = t_trouble.max_in_one_row()
            result.append(max_in_row)
            current_ind = end
        self._write_result(result)

    def get_local_data(self):
        data_input = list(map(self._split_line_to_list, self._iter_input()))
        return data_input


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
        return max(result.items(), key=operator.itemgetter(1))[1]


if __name__ == '__main__':
    # python -m jam.ticket A-large-practice
    TicketSolver(sys.argv[1])()
