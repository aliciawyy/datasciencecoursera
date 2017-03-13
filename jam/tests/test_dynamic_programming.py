from nose_parameterized import parameterized
from numpy.testing import TestCase

from .. import dynamic_programming as dp

import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class DPTest(TestCase):
    def test_get_flower_order(self):
        test_cases = [
            [[5, 4, 3, 2, 1],
             [1, 1, 1, 1, 1],
             [365, 365, 365, 365, 365],
             [1, 2, 3, 4, 5]],
            [[5, 4, 3, 2, 1],
             [1, 5, 10, 15, 20],
             [4, 9, 14, 19, 24],
             [5, 4, 3, 2, 1]],
            [[5, 4, 3, 2, 1],
             [1, 5, 10, 15, 20],
             [5, 10, 15, 20, 25],
             [1, 2, 3, 4, 5]],
            [[5, 4, 3, 2, 1],
             [1, 5, 10, 15, 20],
             [5, 10, 14, 20, 25],
             [3, 4, 5, 1, 2]],
            [[1, 2, 3, 4, 5, 6],
             [1, 3, 1, 3, 1, 3],
             [2, 4, 2, 4, 2, 4],
             [2, 4, 6, 1, 3, 5]],
            [[3, 2, 5, 4],
             [1, 2, 11, 10],
             [4, 3, 12, 13],
             [4, 5, 2, 3]],
        ]
        for i, test_case in enumerate(test_cases):
            self.assert_get_ordering_equal(*test_case)
            log.debug("Test case no. {} succeeded.".format(i))

    def assert_get_ordering_equal(self, height, bloom, wilt, expected):
        result = dp.get_flower_order(height, bloom, wilt)
        self.assertListEqual(result, expected)

    @parameterized.expand(
        [([1, 7, 4, 9, 2, 5], 6),
         ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
         ([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000,
           32, 32], 8),
         ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
         ([44], 1),
         ([374, 40, 854, 203, 203, 156, 362, 279, 812, 955,
           600, 947, 978, 46, 100, 953, 670, 862, 568, 188,
           67, 669, 810, 704, 52, 861, 49, 640, 370, 908,
           477, 245, 413, 109, 659, 401, 483, 308, 609, 120,
           249, 22, 176, 279, 23, 22, 617, 462, 459, 244], 36)
         ]
    )
    def test_longest_zig_zag(self, seq, expected):
        self.assertEqual(dp.longest_zig_zag_dp(seq), expected)
