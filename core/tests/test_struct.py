import numpy as np
from numpy.testing import TestCase, assert_array_almost_equal

from data import api
from core import struct


class ProblemTest(TestCase):
    def test_init(self):
        num_samples = 10
        data = np.random.rand(20).reshape(num_samples, 2)
        target = np.ones(num_samples)
        self.assertRaises(ValueError, struct.Problem, data, np.zeros(num_samples + 1))
        pb = struct.Problem(data, target)
        assert_array_almost_equal(pb.data, data)
        assert_array_almost_equal(pb.target, target)

    def test_from_data_frame(self):
        df = api.load_candidates_to_hire_data()
        res = [struct.Problem.from_data_frame(df), struct.Problem.from_data_frame(df, "hire")]
        for pb in res:
            self.assertListEqual(list(pb.target), list(df["hire"]))
            self.assertListEqual(list(pb.data.columns), list(df.columns[:-1]))
