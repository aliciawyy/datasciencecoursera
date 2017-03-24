from numpy.testing import TestCase
from parameterized import parameterized

from .. import quick_sum as qs


class QuickSumTest(TestCase):
    def setUp(self):
        self.quick_sum = qs.QuickSum()

    @parameterized.expand(
        [("99999", 45, 4), ("1110", 3, 3), ("0123456789", 45, 8),
         ("99999", 100, -1), ("382834", 100, 2), ("9230560001", 71, 4)]
    )
    def test_min_sums(self, numbers, n_sum, expected):
        self.assertEqual(self.quick_sum.min_sums(numbers, n_sum), expected)
