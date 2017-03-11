from numpy.testing import TestCase

from .. import algo


class AlgorithmTest(TestCase):
    def test_get_local_data(self):
        result = algo.get_local_data()
        self.assertListEqual(result, [])


class TicketTroubleTest(TestCase):
    def test_case1(self):
        n_friend, n_grid = 3, 3
        tickets = [[1, 2],
                   [2, 3],
                   [2, 2]]
        self._assert_max_equal(n_grid, tickets, 3)

    def test_case2(self):
        tickets = [[1, 2], [1, 2]]
        self._assert_max_equal(3, tickets, 1)

    def _assert_max_equal(self, n_grid, tickets, expected):
        t_trouble = algo.TicketTrouble(n_grid, tickets)
        self.assertEqual(t_trouble.max_in_one_row(), expected)

    def test_solve(self):
        algo.solve(*algo.get_local_data('A-large'))
