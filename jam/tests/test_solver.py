from numpy.testing import TestCase
from ..util import SolverBase

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class SolverTest(TestCase):

    def test_sample_same_as_ref(self):
        for sub in SolverBase.__subclasses__():
            log.debug('Test class {}'.format(sub.__name__))
            solver = sub("sample")
            self._assert_sample_same_as_ref(solver)

    def _assert_sample_same_as_ref(self, solver):
        solver()
        with solver._get_file_handler("out.ref") as f_ref:
            with open(solver.get_filename('out'), "r") as f_out:
                for line_ref, line_out in zip(f_ref, f_out):
                    self.assertEqual(line_ref, line_out)
