import pandas as pd
from sklearn import cross_validation
import dm_common


class Problem(dm_common.StringMixin):
    def __init__(self, data, target):
        if data.shape[0] != len(target):
            raise ValueError("Then length of data '{}' and the length of target '{}' are not "
                             "equal.".format(data.shape[0], len(target)))
        self._data = data
        self._target = target

    @classmethod
    def from_data_frame(cls, df, target_col=None):
        if target_col is None:
            target_col = df.columns[-1]  # take the last column as target by default
        return cls(df.drop(target_col, 1), df[target_col])

    @property
    def data(self):
        return self._data

    @property
    def target(self):
        return self._target

    def train_test_split(self, test_size=0.2, random_state=0):
        x_train, x_test, y_train, y_test = cross_validation.train_test_split(
            self.data, self.target, test_size=test_size, random_state=random_state)
        problem_train = Problem(x_train, y_train)
        problem_test = Problem(x_test, y_test)
        return problem_train, problem_test

