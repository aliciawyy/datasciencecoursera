from numpy.testing import TestCase

from .. import dynamic_programming as dp

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class FlowerGardenTest(TestCase):
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
