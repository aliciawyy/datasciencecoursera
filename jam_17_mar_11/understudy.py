from os import path
import sys
import numpy as np

DATA_DIR = path.join(path.dirname(__file__), "..", "data", "understudy")


def get_local_data(name="sample"):
    filename1 = path.join(DATA_DIR, name + ".in")
    f = file(filename1, "r")
    n_sample = int(f.readline())
    prob_absent_list = []
    for i, line in enumerate(f.readlines()):
        if i % 2 == 1:
            prob_absent = [float(s) for s in line.split(" ")]
            prob_absent_list.append(prob_absent)
    return prob_absent_list, name


def solve(prob_absent_list, name):
    out_file = file(path.join(DATA_DIR, name + ".out"), "w")
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
    solve(*get_local_data(sys.argv[1]))
