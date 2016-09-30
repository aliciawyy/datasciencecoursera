import numpy as np
from numpy.testing import TestCase, assert_array_almost_equal

from core import util


class UtilTest(TestCase):
    def test_entropy(self):
        x = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1]
        self.assertEqual(util.entropy(x), 0.41381685030363374)
        self.assertEqual(util.entropy(np.ones(10)), .0)
        x = [0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
        self.assertEqual(util.entropy(x), 1.)


def test_information_gain1():
    x = np.array([[0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
                  [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]]).transpose()
    y = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1]
    res = util.information_gain(x, y)
    assert_array_almost_equal(res, [0.654858,  0.979869])


def test_information_gain2():
    x = np.array([0, 1, 0])
    y = [0, 1, 0]
    res = util.information_gain(x, y)
    assert_array_almost_equal(res, [0.918296])



