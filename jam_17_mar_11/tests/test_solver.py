from os import path
from numpy.testing import TestCase

from ..ticket import TicketSolver
from ..understudy import UnderStudySolver
from ..word import WordSolver


class SolverTest(TestCase):

    def test_sample_same_as_ref(self):
        for sub in [TicketSolver, UnderStudySolver, WordSolver]:
            solver = sub("sample")
            self._assert_sample_same_as_ref(solver)

    def _assert_sample_same_as_ref(self, solver):
        solver()
        out_filename = path.join(solver.data_dir, solver.name + ".out")
        with solver._get_file_handler("out.ref") as f_ref:
            with open(out_filename, "r") as f_out:
                for line_ref, line_out in zip(f_ref, f_out):
                    self.assertEqual(line_ref, line_out)
