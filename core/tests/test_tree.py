import functools
from numpy.testing import TestCase, assert_array_almost_equal

from core import tree
from data import api


class DecisionTreeTest(TestCase):
    def setUp(self):
        full_data = api.load_candidates_to_hire_data()
        target_tag = "hire"
        self.ch_target = full_data[target_tag]
        self.ch_data = full_data.drop(target_tag, 1)
        self.id3_expected = ("level", {
            "Junior": ('phd', {None: True, 'no': True, 'yes': False}),
            "Mid": True,
            "Senior": ('tweets', {None: False, 'no': False, 'yes': True}),
            None: True
        })

    def test_fit_id3(self):
        result = tree.fit_id3(self.ch_data, self.ch_target)
        self.assertTupleEqual(result, self.id3_expected)

    def test_fit_id3_gini(self):
        id3 = tree.ID3("gini")
        id3.fit(self.ch_data, self.ch_target)
        self.assertTupleEqual(id3.root, self.id3_expected)

    def test_predict_id3(self):
        predict = functools.partial(tree.predict_id3, self.id3_expected)
        self.assertFalse(predict({"level": "Junior", "lang": "R", "tweets": "no", "phd": "yes"}))
        self.assertTrue(predict({"level": "Mid", "lang": "R", "tweets": "no", "phd": "yes"}))
        self.assertFalse(predict({"level": "Senior", "lang": "R", "tweets": "no", "phd": "yes"}))
        self.assertTrue(predict({"level": "Senior", "lang": "R", "tweets": "yes", "phd": "yes"}))
        self.assertTrue(predict({"level": "Intern", "lang": "java", "tweets": "yes", "phd": "yes"}))
        self.assertTrue(predict({"lang": "java", "tweets": "yes", "phd": "yes"}))
        self.assertFalse(predict({"level": "Senior", "lang": "R"}))

    def test_class_ID3(self):
        id3 = tree.ID3()
        id3.fit(self.ch_data, self.ch_target)
        self.assertTrue(id3.predict({"level": "Mid", "lang": "R", "tweets": "no", "phd": "yes"}))
        self.assertFalse(
            id3.predict({"level": "Senior", "lang": "R", "tweets": "no", "phd": "yes"}))

    def test_init_raises(self):
        self.assertRaises(NotImplementedError, tree.ID3, criterion="dummy")
