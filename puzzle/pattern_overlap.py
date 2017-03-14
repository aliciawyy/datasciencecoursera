"""
http://code.google.com/codejam/contest/8284486/dashboard#s=p1
"""
import sys
import numpy as np

from . import util


class PatternOverlapSolver(util.SolverBase):

    def __call__(self):
        result = []
        pattern1 = ''
        for i, line in enumerate(self._iter_input()):
            if i % 2 == 0:
                pattern1 = line.rstrip()
            else:
                pattern2 = line.rstrip()
                obj = PatternOverlap(pattern1, pattern2)
                result.append(obj())
        self._write_result(result)


class PatternOverlap(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __call__(self):
        return str(match(self.p1, self.p2) or match(self.p2, self.p1)).upper()


def match(p1, p2):
    idx1 = idx2 = 0
    while idx1 < len(p1) and idx2 < len(p2):
        if p1[idx1] != "*" and p2[idx2] != "*":
            if p1[idx1] != p2[idx2]:
                return False
        elif p1[idx1] == "*":
            if len(p2[idx2:]) <= 4:
                return True
            if idx1 + 1 >= len(p1):
                return False

        idx1 += 1
        idx2 += 1
    if idx1 >= len(p1) and idx2 >= len(p2):
        return True
    elif idx1 >= len(p1):
        return _all_star(p2[idx2:])
    else:
        return _all_star(p1[idx1:])


def _all_star(x):
    return all([c == "*" for c in x])


if __name__ == "__main__":
    # python -m jam.pattern_overlap sample
    PatternOverlapSolver(sys.argv[1])()
