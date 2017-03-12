import numpy as np

from numpy.testing import TestCase, assert_array_equal
from models import metrics


class MCCTest(TestCase):
    def test_eval_mcc(self):
        prob_pred = np.array([.1, .2, .3, .2, .6, .4]).transpose()
        y_pred_expected = [0, 0, 1, 0, 1, 1]
        y_true = np.array([0, 0, 1, 1, 0, 1])
        best_proba, best_mcc, y_pred = metrics.eval_mcc(
            y_true, prob_pred, True
        )
        assert_array_equal(y_pred_expected, y_pred)
        self.assertAlmostEqual(best_proba, 0.2)
        self.assertAlmostEqual(best_mcc, 0.3333333333)
