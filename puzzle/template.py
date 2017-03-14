"""
Replace XXX with the name of problem
"""
import sys

from . import util


class XXXSolver(util.SolverBase):

    def __call__(self):
        result = []
        for line in self._iter_input():
            x = self._split_line_to_list(line, int)
            obj = XXX(x)
            prob = obj()
            result.append(prob)
        self._write_result(result)


class XXX(object):
    def __init__(self):
        pass

    def __call__(self):
        return 1


if __name__ == "__main__":
    XXXSolver(sys.argv[1])()
