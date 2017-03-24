from numpy.testing import TestCase
from parameterized import parameterized

from .. import stripe_painter as sp


class StripePainterTest(TestCase):
    def setUp(self):
        self.painter = sp.StripePainter()

    @parameterized.expand(
        [("BECBBDDEEBABDCADEAAEABCACBDBEECDEDEACACCBEDABEDADD", 26),
         ("RGBGR", 3), ("RGRG", 3), ("ABACADA", 4), ("BRGBGR", 4),
         ("AABBCCDDCCBBAABBCCDD", 7)]
    )
    def test_min_strokes(self, stripes, expected):
        self.assertEqual(self.painter.min_strokes(stripes), expected)

