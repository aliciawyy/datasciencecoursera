"""
Operators
"""
import numpy as np
import pandas as pd

import dm_common
import struct
import util


class BaggingClassifier(dm_common.StringMixin):
    def __init__(self, model, n=10, random_state=0):
        self.fittings = [model() for _ in range(n)]
        self.random_state = random_state
        np.random.seed(self.random_state)

    def fit(self, x, y):
        for fitting in self.fittings:
            random_state = self.random_state + np.random.randint(10)
            fitting.fit(*struct.get_bootstrap_sample(x, y, random_state=random_state))

    def predict(self, x):
        votes = [fitting.predict(x) for fitting in self.fittings]
        if isinstance(x, pd.DataFrame):
            df_votes = pd.concat(votes, axis=1)
            return df_votes.apply(util.most_common, axis=1)
        else:
            return util.most_common(votes)

