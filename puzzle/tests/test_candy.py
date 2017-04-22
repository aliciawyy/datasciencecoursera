from parameterized import parameterized
from numpy.testing import TestCase

from .. import candy


class TestCollectCandies(TestCase):
    @parameterized.expand(
        [(5, 5, 12,
          [[2, 1, 1, 1, 1], [2, 2, 1, 1, 1], [1, 2, 1, 1, 1],
           [2, 2, 1, 1, 3], [2, 2, 2, 2, 2]])]
    )
    def test_candy(self, n, m, t, candies):
        collector = candy.CollectCandies(n, m, t, candies)
        for pos, expected in [[(1, 1), [(0, 1), (2, 1), (1, 0), (1, 2)]],
                              [(0, 0), [(1, 0), (0, 1)]],
                              [(4, 4), [(3, 4), (4, 3)]]]:
            self.assertListEqual(
                collector.get_next_positions(pos), expected + [pos])
        self.assertEqual(collector.get_max_sum(), 27)
