import numpy as np


class StripePainter(object):
    def __init__(self):
        self.stripes_ = None

    def __repr__(self):
        return self.stripes_

    def set_stripes(self, stripes):
        # When the same color repeat, only count it once as it can be painted
        # in one stroke
        s = stripes[0]
        for i, c in enumerate(stripes[1:]):
            if c != s[-1]:
                s += c
        self.stripes_ = s

    def min_strokes(self, stripes):
        self.set_stripes(stripes)
        n = len(self.stripes_)
        # n_strokes is a state matrix that shows how many moves are needed
        # from the position i to j
        # From i to i we always need one stroke
        n_strokes = np.zeros((n, n), dtype=np.int8) + np.eye(n, dtype=np.int8)
        for j, color_end in enumerate(self.stripes_[1:], 1):
            for i in range(j - 1, -1, -1):
                min_strokes = n
                for k in range(i, j):
                    # All the (i, k) k < j are computed in the previous loops
                    # of j, all the (k + 1, j) k > i are computed in the
                    # previous loops of i
                    current_n_strokes = n_strokes[i, k] + n_strokes[k + 1, j]
                    min_strokes = min(current_n_strokes, min_strokes)
                if color_end == self.stripes_[i]:
                    # if color end is equal to the color start, we can merge
                    # the two sections into one by removing one stroke
                    min_strokes -= 1
                n_strokes[i, j] = min_strokes

        return n_strokes[0, n - 1]


def is_symmetric(stripes):
    for i in range(int(len(stripes) / 2)):
        if stripes[i] != stripes[-1 - i]:
            return False
    return True
