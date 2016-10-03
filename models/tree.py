"""
Tree algorithm
"""
import functools
import pandas as pd
import numpy as np

import dm_common
import struct
import util


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


class RandomForest(dm_common.StringMixin):
    def __init__(self, num_trees=10, random_state=0):
        self.trees = [ID3() for _ in range(num_trees)]
        self.random_state = random_state
        np.random.seed(self.random_state)

    def fit(self, x, y):
        for current_tree in self.trees:
            random_state = self.random_state + np.random.randint(10)
            current_tree.fit(*struct.get_bootstrap_sample(x, y, random_state=random_state))

    def predict(self, x):
        votes = [current_tree.predict(x) for current_tree in self.trees]
        if isinstance(x, pd.DataFrame):
            df_votes = pd.concat(votes, axis=1)
            return df_votes.apply(util.most_common, axis=1)
        else:
            return util.most_common(votes)

