import collections
from scipy.special import comb
import numpy as np


def _iter_key_sorted_dct(dct):
    for k in sorted(dct.keys()):
        yield k, dct[k]


def make_sum(dct_values, base=None):
    """base is some previous result"""
    sum_cnt = collections.defaultdict(int)
    if base is not None:
        sum_cnt.update(base)
    for v, n in _iter_key_sorted_dct(dct_values):
        # to include from 1 to n elements of value v
        dct = dict(sum_cnt)
        for i in range(1, n + 1):
            n_ways = comb(n, i)
            increment = i * v  # increment for sum by including n times v
            sum_cnt[increment] += n_ways
            for k, v_orig in _iter_key_sorted_dct(dct):
                sum_cnt[k + increment] += n_ways * v_orig
    return sum_cnt


class Jewelry(object):
    def __init__(self):
        self.base = [0, 1]
        self.values_ = None
        self.aux_ = {}

        self.ways_below_ = collections.defaultdict(int)
        self.ways_below_[0] = 1

    def __repr__(self):
        return repr(self.values_)

    def set_values(self, v):
        self.values_ = collections.Counter(v)

    def how_many(self, values):
        self.set_values(values)
        count = 0
        values_for_above = dict(self.values_)

        for v, cnt in _iter_key_sorted_dct(self.values_):
            # Remove value v iteratively to get all the possible sums from
            # the values above v
            values_for_above.pop(v)
            ways_above_exclude_v = make_sum(values_for_above)
            ways_below_exclude_v = dict(self.ways_below_)
            for i in range(1, cnt + 1):
                n_ways = comb(cnt, i)
                ways_below = collections.defaultdict(int)
                for k, cnt_orig in _iter_key_sorted_dct(ways_below_exclude_v):
                    sum_with_iv = k + v * i
                    cnt_increment = n_ways * cnt_orig
                    ways_below[sum_with_iv] += cnt_increment
                    self.ways_below_[sum_with_iv] += cnt_increment
                # The ways above can include cnt - i elements in maximum
                ways_above = make_sum({v: cnt - i}, ways_above_exclude_v)
                intersection = set(ways_below).intersection(ways_above)
                count += np.sum([ways_below[k] * ways_above[k]
                                 for k in intersection])
        return count
