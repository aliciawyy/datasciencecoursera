"""
Tree algorithm
"""
import numpy as np

import dm_common
import util


def fit_id3(x, y):
    # x, y are supposed to be pandas DataFrame format
    # ig = information gain
    ig_by_feature = util.information_gain(x, y)
    max_ig_feature = np.argmax(ig_by_feature)
    root = {}
    for feature in x[max_ig_feature].unique():
        subset = x[max_ig_feature] == feature
        y_subset = y[subset]
        if util.almost_zero(util.entropy(y_subset)) or x.shape[1] == 1:
            root[feature] = y_subset.value_counts().idxmax()
        else:
            x_subset = x.drop(max_ig_feature, 1).ix[subset]
            root[feature] = fit_id3(x_subset, y_subset)
    return max_ig_feature, root


def predict_id3(decision_tree, x):
    answer = x[decision_tree[0]]
    node = decision_tree[1][answer]
    return predict_id3(node, x) if isinstance(node, tuple) else node


class ID3(dm_common.StringMixin):
    """
    Iterative Dichotomiser 3
    https://en.wikipedia.org/wiki/ID3_algorithm
    """

    def __init__(self):
        self.root = None

    def fit(self, x, y):
        self.root = fit_id3(x, y)

    def predict(self, x):
        return predict_id3(self.root, x)




