from __future__ import division
import numpy as np
import pandas as pd
from numpy.testing import TestCase, assert_array_almost_equal

from core import util


class UtilTest(TestCase):
    def test_entropy(self):
        x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        self.assertEqual(util.entropy(x), 0.41381685030363374)
        self.assertEqual(util.entropy(np.ones(10)), .0)
        x = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
        self.assertEqual(util.entropy(x), 1.)

    def test_group_probability(self):
        x = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
        result = util.group_probability(x)
        self.assertDictEqual(result, {0: .5, 1: .5})
        self.assertDictEqual(util.group_probability(np.ones(10)), {1: 1})

    def test_gini(self):
        x = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
        self.assertAlmostEqual(util.gini(x), 0.5)
        self.assertAlmostEqual(util.gini(np.zeros(10)), 0.)
        x = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0]
        expected = np.sum(x) / len(x)
        expected = 2 * (1. - expected) * expected
        self.assertAlmostEqual(util.gini(x), expected)

    def test_almost_zero(self):
        self.assertFalse(util.almost_zero(1e-5))
        self.assertTrue(util.almost_zero(1e-5, 1e-4))

    def test_information_gain_raises(self):
        self.assertRaises(NotImplementedError, util.information_gain, [], [])


def test_information_gain1():
    x = np.array([[0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
                  [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]]).transpose()
    df_x = pd.DataFrame(x)
    y = pd.Series([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1])
    res = util.information_gain(df_x, y)
    assert_array_almost_equal(res, [0.654858,  0.979869])


def test_information_gain2():
    x = np.array([0, 1, 0])
    y = np.array([0, 1, 0])
    res = util.information_gain(x, y)
    assert_array_almost_equal(res, [0.918296])



