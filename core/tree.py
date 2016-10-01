"""
Tree algorithm
"""
import functools
import numpy as np

import dm_common
import util


def fit_id3(x, y):
    # x, y are supposed to be pandas DataFrame format
    partition_entropy = functools.partial(util.partition_entropy, y=y)
    entropy_by_feature = x.apply(partition_entropy)
    min_entropy_feature = np.argmin(entropy_by_feature)
    root = {None: y.value_counts().idxmax()}  # default case
    for feature in x[min_entropy_feature].unique():
        subset = x[min_entropy_feature] == feature
        y_subset = y[subset]
        if util.almost_zero(util.entropy(y_subset)) or x.shape[1] == 1:
            root[feature] = y_subset.value_counts().idxmax()
        else:
            x_subset = x.drop(min_entropy_feature, 1).ix[subset]
            root[feature] = fit_id3(x_subset, y_subset)
    return min_entropy_feature, root


def predict_id3(decision_tree, x):
    answer = x.get(decision_tree[0], None)
    node = decision_tree[1].get(answer, decision_tree[1][None])
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




