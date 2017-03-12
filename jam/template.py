import sys

from .util import SolverBase


class XXXSolver(SolverBase):

    def __call__(self):
        result = []
        for line in self._iter_input():
            x = self._split_line_to_list(line, int)
            xxx_obj = XXX(x)
            prob = xxx_obj()
            result.append(prob)
        self._write_result(result)


class XXX(object):
    def __init__(self, x):
        pass

    def __call__(self):
        return 1


if __name__ == "__main__":
    XXXSolver(sys.argv[1])()
