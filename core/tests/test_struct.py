import numpy as np
from numpy.testing import TestCase, assert_array_almost_equal

from data import api
from core import struct


class ProblemTest(TestCase):

    def setUp(self):
        self.df = api.load_candidates_to_hire_data()
        self.problem = struct.Problem.from_data_frame(self.df)

    def test_init(self):
        num_samples = 10
        data = np.random.rand(20).reshape(num_samples, 2)
        target = np.ones(num_samples)
        self.assertRaises(ValueError, struct.Problem, data, np.zeros(num_samples + 1))
        pb = struct.Problem(data, target)
        assert_array_almost_equal(pb.data, data)
        assert_array_almost_equal(pb.target, target)
        self.assertEqual(len(pb), 10)

    def test_from_data_frame(self):
        for pb in [self.problem, struct.Problem.from_data_frame(self.df, "hire")]:
            self.assertListEqual(list(pb.target), list(self.df["hire"]))
            self.assertListEqual(list(pb.data.columns), list(self.df.columns[:-1]))

    def test_train_test_split(self):
        pb_train, pb_test = self.problem.train_test_split(0.285714, 0)
        self.assertEqual(len(pb_train.target), 10)
        self.assertEqual(len(pb_train.data), 10)
        self.assertListEqual(list(pb_train.data.index), list(pb_train.target.index))
        self.assertEqual(len(pb_test.data), 4)
        self.assertEqual(len(pb_test.target), 4)
        self.assertListEqual(list(pb_test.data.index), list(pb_test.target.index))

    def test_get_bootstrap_sample(self):
        bootstrap_sample = self.problem.get_bootstrap_sample(10)
        expected_index = [9, 13, 4, 0, 1, 11, 12, 9, 13, 0, 13, 1, 10, 8]
        self.assertListEqual(list(bootstrap_sample.index), expected_index)
        self.assertListEqual(list(bootstrap_sample.data.index), expected_index)
        self.assertListEqual(list(bootstrap_sample.target.index), expected_index)

