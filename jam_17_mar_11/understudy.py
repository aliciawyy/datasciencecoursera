import sys
import numpy as np

from util import SolverBase


class UnderStudySolver(SolverBase):

    def get_local_data(self):
        f = self._get_input_file()
        prob_absent_list = []
        for i, line in enumerate(f.readlines()):
            if i % 2 == 1:
                prob_absent = [float(s) for s in line.split(" ")]
                prob_absent_list.append(prob_absent)
        return prob_absent_list

    def __call__(self):
        prob_absent_list = self.get_local_data()
        out_file = self._get_file_handler('out')
        for i, prob_absent in enumerate(prob_absent_list, 1):
            show_success = ShowSuccess(prob_absent)
            prob = show_success.probability()
            out_file.write("Case #{}: {}\n".format(i, prob))
        out_file.close()


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
