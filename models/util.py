from __future__ import division
import collections
import functools
import numpy as np
import pandas as pd

DISORDER_METRICS = {}


def disorder_metric(func):
    DISORDER_METRICS.update({func.__name__: func})
    return func


def group_probability(x):
    """Compute the probability of each group given an array x"""
    count = collections.Counter(x)
    num_samples = len(x)
    return {k: v / num_samples for k, v in count.items()}


@disorder_metric
def gini(x):
    group_probabilities = list(group_probability(x).values())
    return np.sum(group_probabilities * np.subtract(1, group_probabilities))


@disorder_metric
def entropy(x):
    """
    Entropy is an attribute of a random variable that measures its disorder.
    The higher the entropy is, the higher the disorder is,
    i.e. the less it can be predicted.

    In the binary case, if the probability of an event is 50%,
    it corresponds to the highest disorder.

    A good training set requires higher entropy.
    """
    group_probabilities = list(group_probability(x).values())
    return - np.sum(group_probabilities * np.log2(group_probabilities))


def partition_disorder(partition, y, criterion="entropy"):
    subsets = [y[partition == part] for part in np.unique(partition)]
    num_samples = len(y)
    disorder_metric_func = DISORDER_METRICS[criterion]
    return np.sum(len(v) / num_samples * disorder_metric_func(v)
                  for v in subsets)


def information_gain(x, y):
    """
    Information gain tells us how important a given feature is. It is used 
    when we want to determine which attribute in a given set of training 
    feature vectors is most useful for discriminating
    between the classes to be learned.

    Information gain is defined as IG(x, y) = H(y) - H(y|x)

    The conditional entropy of y given x is

    H(y|x) = sum( p(x = X_i) * H(y| x = X_i) )

    H(y|x) can also be interpreted as the weighted average of children entropy
    """
    disorder_measure = functools.partial(partition_disorder, y=y)
    if isinstance(x, np.ndarray):
        x = x.T if x.ndim == 1 else x
        res = np.apply_along_axis(disorder_measure, axis=0, arr=x)
    elif isinstance(x, pd.DataFrame):
        res = x.apply(disorder_measure)
    else:
        raise NotImplementedError(
            "Type x = {} is not implemented.".format(type(x))
        )
    return np.subtract(entropy(y), res)


def almost_zero(x, epsilon=1e-10):
    return np.abs(x) < epsilon


def most_common(x):
    return collections.Counter(x).most_common(1)[0][0]
