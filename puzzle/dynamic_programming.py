"""
- https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
get_flower_order

- https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
longest_zig_zag

- https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009
max_donation_from_neighbors

- https://community.topcoder.com/stat?c=problem_statement&pm=1592&rd=4482



"""
import numpy as np


def get_flower_order(height, bloom, wilt):
    # Sort the flowers to make the height in ascending order
    flowers = sorted(zip(height, bloom, wilt))

    def is_overlap(f1, f2):
        # There is overlap when start1 <= end2 and start2 <= end1
        return f1[1] <= f2[2] and f2[1] <= f1[2]

    ordered = []
    for i, f in enumerate(flowers):
        pos = i
        # All the flowers are ordered before i
        while pos > 0 and not is_overlap(f, ordered[pos - 1]):
            pos -= 1
        ordered.insert(pos, f)
    result = [f[0] for f in ordered]
    return result


def longest_zig_zag(seq):
    """
    The complexity is n2 with DP.
    Auxiliary Space is n.
    """
    def to_sign(first, second):
        if first < second:
            return -1
        if first > second:
            return 1
        else:
            return 0

    n = len(seq)
    if n <= 2:
        return n

    longest_len = [0] * n
    longest_len[0] = 1
    longest_len[1] = 2
    last_diff_sign = [-1] * n
    last_diff_sign[1] = to_sign(seq[0], seq[1])

    max_longest_len = 2
    for i, item in enumerate(seq[2:], 2):
        max_len = 0
        for j in range(i):
            current_sign = to_sign(seq[j], item)
            if last_diff_sign[j] * current_sign == -1:
                if longest_len[j] + 1 > max_len:
                    max_len = longest_len[j] + 1
                    last_diff_sign[i] = current_sign
        longest_len[i] = max_len
        max_longest_len = max(max_longest_len, max_len)
    return max_longest_len


def max_donation_from_neighbors(donations):
    # init
    dons = np.array(donations, dtype=np.int16)
    dons = np.roll(dons, -np.argmax(dons))

    first_element_in = [True] * len(dons)
    first_element_in[1] = False
    max_list = list(dons)

    max_donation = max_list[0]
    for i, donation_i in enumerate(dons[2:-1], 2):
        max_i = max_list[0] + donation_i
        for j in range(1, i - 1):
            max_j = max_list[j] + donation_i
            if max_j > max_i:
                max_i = max_j
                first_element_in[i] = first_element_in[j]
        max_list[i] = max_i
        max_donation = max(max_donation, max_i)

    last_donation = dons[-1]
    for i, don_i in enumerate(dons[1:-2]):
        if not first_element_in[i]:
            max_donation = max(max_donation, last_donation + don_i)
    return max_donation


class ChessMetric(object):
    def __init__(self):
        x_change = [[i, j] for i in range(-1, 2)
                    for j in range(-1, 2) if i != 0 or j != 0]
        l_change_aux = np.array([[i, j] for i in [-1, 1] for j in [-1, 1]],
                                dtype=np.int8)
        l_change_h = np.multiply([2, 1], l_change_aux)
        l_change_v = np.multiply([1, 2], l_change_aux)
        self.possible_pos_change = np.concatenate(
            (x_change, l_change_h, l_change_v)
        )

    def get_next_positions(self, pos, board_size):
        def _on_board(x_col):
            return (x_col >= 0) & (x_col < board_size)

        previous_pos = np.add(self.possible_pos_change, pos)
        pos_on_board = _on_board(previous_pos[:, 0]) & \
            _on_board(previous_pos[:, 1])
        return previous_pos[pos_on_board]

    def how_many_paths(self, board_size, start, end, num_moves):
        # num_moves will be between 1 and 50 inclusive
        num_paths = np.zeros((board_size, board_size), dtype=np.int64)
        pos_dct = {tuple(start): 1}
        for i in range(num_moves):
            new_pos_set = set()
            for pos, pos_num_path in pos_dct.items():
                next_pos = self.get_next_positions(pos, board_size)
                num_paths[list(zip(*next_pos))] += pos_num_path
                new_pos_set = new_pos_set.union(map(tuple, next_pos))
            new_pos_set = list(new_pos_set)
            pos_dct = dict(
                zip(new_pos_set, num_paths[list(zip(*new_pos_set))])
            )
        return num_paths[end[0], end[1]]


class AvoidRoads(object):
    def __init__(self):
        self.possible_moves = np.array([[1, 0], [0, 1]], dtype=np.int8)
        self.bad_ = None
        self.width_ = 0
        self.height_ = 0

    def get_next_positions(self, pos):
        next_pos = self.possible_moves + pos
        selection = (next_pos[:, 0] < self.width_) & \
                    (next_pos[:, 1] < self.height_)
        next_pos = next_pos[selection]
        next_pos = list(map(tuple, next_pos))
        bad_pos = self.bad_.get(pos, None)
        if bad_pos is not None:
            next_pos.remove(bad_pos)
        return next_pos

    def set_bad(self, bad):
        bad = [list(map(int, p.split(" "))) for p in bad]
        self.bad_ = dict(sorted([tuple(p[:2]), tuple(p[2:])]) for p in bad)

    def set_dimension(self, w, h):
        self.width_ = w + 1
        self.height_ = h + 1

    def num_ways(self, width, height, bad):
        self.set_bad(bad)
        self.set_dimension(width, height)
        num_paths = np.zeros((self.width_, self.height_), dtype=np.int64)
        pos_dct = {(0, 0): 1}
        n = self.width_ + self.height_
        for i in range(n):
            new_pos_set = set()
            for pos, pos_num_path in pos_dct.items():
                next_pos = self.get_next_positions(pos)
                num_paths[list(zip(*next_pos))] += pos_num_path
                new_pos_set = new_pos_set.union(next_pos)
            new_pos_set = list(new_pos_set)
            pos_dct = dict(
                zip(new_pos_set, num_paths[list(zip(*new_pos_set))])
            )
        return num_paths[-1, -1]
