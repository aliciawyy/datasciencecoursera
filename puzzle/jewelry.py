import itertools
import collections
import numpy as np


class Jewelry(object):
    def __init__(self):
        self.base = [0, 1]
        self.values_ = None
        self.aux_ = {}

    def __repr__(self):
        return repr(self.values_)

    def set_values(self, v):
        self.values_ = sorted(v)

    def get_auxiliary_vector(self, n):
        if n not in self.aux_:
            self.aux_[n] = np.array(
                list(itertools.product(self.base, repeat=n)), dtype=np.uint32
            )
        return self.aux_[n]

    def make_sum(self, v, last_element=0):
        aux = self.get_auxiliary_vector(len(v))
        v_sum = np.dot(aux, v) + last_element
        return collections.Counter(v_sum)

    def how_many(self, values):
        self.set_values(values)
        count = 0
        num_ways = 0
        for i, bob_last_jewelry in enumerate(self.values_[:-1]):
            # When i is the largest element for Bob
            bob = self.make_sum(self.values_[:i], bob_last_jewelry)
            frank = self.make_sum(self.values_[i + 1:])
            intersection = set(bob.keys()).intersection(frank.keys())
            num_ways = np.sum([frank[s] * bob[s] for s in intersection],
                              dtype=np.uint64)
            count += num_ways
        # if the last value is the same as the second to last, it is possible
        # to give it to Bob
        if self.values_[-1] == self.values_[-2]:
            count += num_ways
        return count






