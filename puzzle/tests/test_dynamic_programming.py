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
        self.assertEqual(dp.longest_zig_zag(seq), expected)

    @parameterized.expand(
        [([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], 16),
         ([10, 3, 2, 5, 7, 8], 19),
         ([11, 15], 15),
         ([7, 7, 7, 7, 7, 7, 7], 21),
         ([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61,
           6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397,
           52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72], 2926)
         ]
    )
    def test_max_donation_from_neighbors(self, donations, expected):
        self.assertEqual(dp.max_donation_from_neighbors(donations), expected)


class ChessMetricTest(TestCase):
    def setUp(self):
        self.chess = dp.ChessMetric()

    def test_possible_pos_change(self):
        self.assertEqual(len(self.chess.possible_pos_change), 16)

    def test_get_next_positions(self):
        pos = [3, 3]
        board_size = 5
        result = self.chess.get_next_positions(pos, board_size)
        self.assertEqual(len(result), 12)

    @parameterized.expand(
        [(100, [0, 0], [0, 99], 50, 243097320072600),  # 32 sec
         (5, [0, 0], [0, 0], 2, 5),
         (3, [0, 0], [2, 2], 1, 0),
         (3, [0, 0], [1, 0], 1, 1), (3, [0, 0], [1, 2], 1, 1)
         ]
    )
    def test_how_many_paths(self, board_size, start, end, num_moves, expected):
        result = self.chess.how_many_paths(board_size, start, end, num_moves)
        self.assertEqual(result, expected)


class AvoidRoadsTest(TestCase):
    def setUp(self):
        self.avoid_r = dp.AvoidRoads()

    @parameterized.expand(
        [(6, 6, ["0 0 0 1", "6 6 5 6"], 252),
         (2, 2, ["0 0 1 0", "1 2 2 2", "1 1 2 1"], 0),
         (1, 1, [], 2),
         (31, 35, [], 6406484391866534976)
         ]
    )
    def test_num_ways(self, w, h, bad, expected):
        result = self.avoid_r.num_ways(w, h, bad)
        self.assertEqual(result, expected)

    def test_sort_bad(self):
        self.avoid_r.set_bad(["0 0 0 1", "6 6 5 6"])
        self.assertDictEqual(
            self.avoid_r.bad_,
            {(0, 0): (0, 1), (5, 6): (6, 6)}
        )
