"""
util functions
"""
from __future__ import division
import collections
import numpy as np
import pandas as pd


def group_probability(x):
    """Compute the probability of each group given an array x"""
    count = collections.Counter(x)
    num_samples = len(x)
    return {k: v / num_samples for k, v in count.items()}


def gini(x):
    group_probabilities = group_probability(x).values()
    return np.sum(group_probabilities * np.subtract(1, group_probabilities))


def entropy(x):
    """
    Entropy is an attribute of a random variable that measures its disorder. The higher the entropy
    is, the higher the disorder is, i.e. the less it can be predicted.

    In the binary case, if the probability of an event is 50%, it corresponds to the highest
    disorder.

    A good training set requires higher entropy.
    """
    group_probabilities = group_probability(x).values()
    return - np.sum(group_probabilities * np.log2(group_probabilities))


def partition_entropy(partition, y):
    num_samples = len(y)
    subsets = collections.defaultdict(list)
    for group, response in zip(partition, y):
        subsets[group].append(response)
    return np.sum(len(v) / num_samples * entropy(v) for v in subsets.values())


def information_gain(x, y):
    """
    Information gain tells us how important a given feature is. It is used when we want to determine
    which attribute in a given set of training feature vectors is most useful for discriminating
    between the classes to be learned.

    Information gain is defined as IG(x, y) = H(y) - H(y|x)

    The conditional entropy of y given x is

    H(y|x) = sum( p(x = X_i) * H(y| x = X_i) )

    H(y|x) can also be interpreted as the weighted average of children entropy
    """
    if isinstance(x, np.ndarray):
        x = x[:, None] if x.ndim == 1 else x
        res = [partition_entropy(x[:, j], y) for j in range(x.shape[1])]
    elif isinstance(x, pd.DataFrame):
        res = x.apply(lambda feature: partition_entropy(feature, y))
    else:
        raise NotImplementedError("Type x = {} is not implemented.".format(type(x)))
    return np.subtract(entropy(y), res)


def almost_zero(x, epsilon=1e-10):
    return np.abs(x) < epsilon
