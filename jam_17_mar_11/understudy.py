import sys
import numpy as np

from util import SolverBase


class UnderStudySolver(SolverBase):

    def __call__(self):
        result = []
        f = self._get_input_file()
        for i, line in enumerate(f.readlines()):
            if i % 2 == 0:
                continue
            prob_absent = [float(s) for s in line.split(" ")]
            show_success = ShowSuccess(prob_absent)
            prob = show_success.probability()
            j_case = i / 2 + 1
            result.append("Case #{}: {}\n".format(j_case, prob))
        f.close()
        self._write_result(result)


class ShowSuccess(object):
    def __init__(self, prob_absent):
        self.prob_absent = prob_absent
        self.n_role = len(self.prob_absent) / 2

    def probability(self):
        prob_absent = np.sort(self.prob_absent)
        role_success = 1. - \
            prob_absent[:self.n_role] * prob_absent[-1:-self.n_role-1:-1]
        return np.prod(role_success)


if __name__ == "__main__":
    # python understudy.py B-large-practice
    UnderStudySolver(sys.argv[1])()
