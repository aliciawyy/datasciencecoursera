"""
Tree algorithm
"""
import functools
import pandas as pd
import numpy as np

import dm_common
import struct
import util
import operator


def fit_id3(x, y, criterion="entropy"):
    # x, y are supposed to be pandas DataFrame format
    partition_disorder = functools.partial(util.partition_disorder, y=y, criterion=criterion)
    disorder_by_feature = x.apply(partition_disorder)
    min_disorder_feature = np.argmin(disorder_by_feature)
    root = {None: y.value_counts().idxmax()}  # default case
    for feature in x[min_disorder_feature].unique():
        subset = x[min_disorder_feature] == feature
        y_subset = y[subset]
        if util.almost_zero(util.entropy(y_subset)) or x.shape[1] == 1:
            root[feature] = y_subset.value_counts().idxmax()
        else:
            x_subset = x.drop(min_disorder_feature, 1).ix[subset]
            root[feature] = fit_id3(x_subset, y_subset)
    return min_disorder_feature, root


def predict_id3(decision_tree, x):
    answer = x.get(decision_tree[0], None)
    node = decision_tree[1].get(answer, decision_tree[1][None])
    return predict_id3(node, x) if isinstance(node, tuple) else node


class ID3(dm_common.StringMixin):
    """
    Iterative Dichotomiser 3
    https://en.wikipedia.org/wiki/ID3_algorithm
    """

    def __init__(self, criterion="entropy"):
        if criterion not in util.DISORDER_METRICS:
            raise NotImplementedError("criterion = '{}' is not among the available disorder "
                                      "metrics: {}".format(criterion, util.DISORDER_METRICS.keys()))
        self.criterion = criterion
        self.root = None

    def fit(self, x, y):
        self.root = fit_id3(x, y, self.criterion)

    def predict(self, x):
        predict_with_root = functools.partial(predict_id3, self.root)
        if isinstance(x, pd.DataFrame):
            result = {k: predict_with_root(v) for k, v in x.to_dict(orient='index').items()}
            return pd.Series(result)
        return predict_with_root(x)


class BootstrapRandomForest(operator.BaggingClassifier):
    def __init__(self, num_trees=10, random_state=0):
        super(self.__class__, self).__init__(ID3, num_trees, random_state)

