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
        self.pos_unchecked_ = {(i, j) for i in range(self.dim[0])
                               for j in range(self.dim[1])}

    def _in_range_x(self, point):
        return 0 <= point[0] < self.dim[0]

    def _in_range_y(self, point):
        return 0 <= point[1] < self.dim[1]

    def append_previous_pos_(self, point):
        def _add(p1):
            self.new_pos_from_previous_[p1].add(point)

        self.pos_unchecked_.remove(point)
        x, y = point[0], point[1]
        map(_add, filter(self._in_range_x, [(x - 1, y), (x + 1, y)]))
        map(_add, filter(self._in_range_y, [(x, y - 1), (x, y + 1)]))
        _add(point)

    def get_max_sum(self):
        if self.time_limit < self.dim[0] + self.dim[1] - 2:
            return "Too late"
        for i in range(self.time_limit):
            if self.pos_unchecked_:
                map(self.append_previous_pos_,
                    self.pos_unchecked_.intersection(self.v_grid_))
            new_values = {
                new_pos: max(
                    map(self.v_grid_.__getitem__, previous_pos_list)
                ) + self.candies[new_pos[0]][new_pos[1]]
                for new_pos, previous_pos_list in
                self.new_pos_from_previous_.items()}
            self.v_grid_.update(new_values)
        return self.v_grid_[(self.dim[0] - 1, self.dim[1] - 1)]


collector = CollectCandies(N, M, T, candies_)
print collector.get_max_sum()