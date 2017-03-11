from numpy.testing import TestCase

from .. import understudy


class ShowSuccessTest(TestCase):
    def test_solve_small(self):
        name = "B-small-practice"
        self._solve(name)

    def test_solve(self):
        name = "B-large-practice"
        self._solve(name)

    def _solve(self, name):
        understudy.solve(*understudy.get_local_data(name))
