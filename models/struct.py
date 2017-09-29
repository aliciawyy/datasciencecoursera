from sklearn import model_selection
import xgboost as xgb
import dm_common


def get_bootstrap_sample(x, y, random_state=0):
    # x should be of type pandas DataFrame
    x_bootstrap = x.sample(len(x), random_state=random_state, replace=True)
    return x_bootstrap, y[x_bootstrap.index]


class Problem(dm_common.StringMixin):
    def __init__(self, data, target):
        if data.shape[0] != len(target):
            raise ValueError("Then length of data '{}' and the length"
                             " of target '{}' are not "
                             "equal.".format(data.shape[0], len(target)))
        self.data = data
        self.target = target

    @classmethod
    def from_data_frame(cls, df, target_col=None):
        if target_col is None:
            # take the last column as target by default
            target_col = df.columns[-1]
        return cls(df.drop(target_col, 1), df[target_col])

    @property
    def index(self):
        return self.data.index

    def train_test_split(self, test_size=0.2, random_state=0):
        x_train, x_test, y_train, y_test = model_selection.train_test_split(
            self.data, self.target, test_size=test_size,
            random_state=random_state
        )
        problem_train = Problem(x_train, y_train)
        problem_test = Problem(x_test, y_test)
        return problem_train, problem_test

    def get_bootstrap_sample(self, random_state=0):
        return Problem(*get_bootstrap_sample(self.data, self.target,
                                             random_state))

    def to_xgb_matrix(self):
        return xgb.DMatrix(self.data, label=self.target)

    def __len__(self):
        return len(self.target)

