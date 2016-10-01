from numpy.testing import TestCase, assert_array_almost_equal

from core import tree
from data import api


class DecisionTreeTest(TestCase):
    def setUp(self):
        full_data = api.load_candidates_to_hire_data()
        target_tag = "hire"
        self.target = full_data[target_tag]
        self.data = full_data.drop(target_tag, 0)