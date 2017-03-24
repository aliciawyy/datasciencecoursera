from parameterized import parameterized
from numpy.testing import TestCase
from .. import util

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class SolverTest(TestCase):

    def test_sample_same_as_ref(self):
        for sub in util.SolverBase.__subclasses__():
            log.debug('Test class {}'.format(sub.__name__))
            solver = sub("sample")
            self._assert_sample_same_as_ref(solver)

    def _assert_sample_same_as_ref(self, solver):
        solver()
        with solver._get_file_handler("out.ref") as f_ref:
            with open(solver.get_filename('out'), "r") as f_out:
                for line_ref, line_out in zip(f_ref, f_out):
                    self.assertEqual(line_ref, line_out)


class UtilTest(TestCase):
    @parameterized.expand(
        [(100, None, 5050), (99, None, 4950), (99, 100, 50)]
    )
    def test_sum_of_int(self, n, mod, expected):
        self.assertEqual(util.sum_of_int(n, mod), expected)

    @parameterized.expand(
        [(3, None, 14), (4, None, 30), (4, 7, 2)]
    )
    def test_sum_of_int_square(self, n, mod, expected):
        self.assertEqual(util.sum_of_int_square(n, mod), expected)

    @parameterized.expand(
        [(4, None, 100), (5, None, 225), (10, 100, 25)]
    )
    def test_sum_of_int_cube(self, n, mod, expected):
        self.assertEqual(util.sum_of_int_cube(n, mod), expected)
