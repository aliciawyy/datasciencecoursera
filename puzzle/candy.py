# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict


def readline_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


N, M, T = readline_to_list()
candies_ = [readline_to_list() for _ in range(N)]


class CollectCandies(object):
    def __init__(self, n, m, t, candies):
        self.dim = n, m
        self.time_limit = t
        self.candies = candies

        self.v_grid_ = {(0, 0): self.candies[0][0]}

        self.new_pos_from_previous_ = defaultdict(set)
        self.pos_checked_ = set()

    def _is_in_range(self, point):
        return 0 <= point[0] < self.dim[0] and 0 <= point[1] < self.dim[1]

    def append_previous_pos_(self, point):
        self.pos_checked_.add(point)
        x, y = point[0], point[1]
        next_pos = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for p in filter(self._is_in_range, next_pos):
            self.new_pos_from_previous_[p].add(point)
        self.new_pos_from_previous_[point].add(point)

    def get_max_sum(self):
        if self.time_limit < self.dim[0] + self.dim[1] - 2:
            return "Too late"
        grid_size = self.dim[0] * self.dim[1]
        for i in range(self.time_limit):
            if len(self.pos_checked_) < grid_size:
                map(self.append_previous_pos_,
                    set(self.v_grid_).difference(self.pos_checked_))
            new_values = {}
            for new_pos, previous_pos_list in self.new_pos_from_previous_.items():
                new_values[new_pos] = max(
                    self.v_grid_[p] for p in previous_pos_list
                ) + self.candies[new_pos[0]][new_pos[1]]
            self.v_grid_.update(new_values)
        return self.v_grid_[(self.dim[0] - 1, self.dim[1] - 1)]


collector = CollectCandies(N, M, T, candies_)
print collector.get_max_sum()