from numpy.testing import TestCase
from nose_parameterized import parameterized

from .. import palindrome as pl


class ShortPalindromesTest(TestCase):

    @parameterized.expand(
        [("RACE", "ECARACE"), ("TOPCODER", "REDTOCPCOTDER"), ("Q", "Q"),
         ("MADAMIMADAM", "MADAMIMADAM"),
         ("ALRCAGOEUAOEURGCOEUOOIGFA",
          "AFLRCAGIOEOUAEOCEGRURGECOEAUOEOIGACRLFA")
         ]
    )
    def test_shortest(self, base, expected):
        self.assertEqual(pl.shortest_palindromes(base), expected)

    @parameterized.expand(
        [('ECA', '', 'ECA'),
         ("BCX", "DCYX", "BDCYX"),
         ('AGGTAB', 'GXTXAYB', 'AGGXTXAYB'),
         # ('ALRCAGOEUAOE', 'AFGIOOUEOCGR', 'AFLRCAGIOEOUAEOCEGR'),
         ]
    )
    def test_shortest_common_super_sequence(self, a, b, expected):
        self.assertEqual(pl.shortest_common_super_sequence(a, b), expected)

    @parameterized.expand(
        [("ABCDGH", "AEDFHR", "ADH"), ("AGGTAB", "GXTXAYB", "GTAB"),
         ('', '', ''), ('abc', '', '')]
    )
    def test_longest_common_sub_sequence(self, a, b, expected):
        self.assertEqual(pl.longest_common_sub_sequence(a, b), expected)

    @parameterized.expand(
        [("ADH", False), ("AFDFDFA", True), ("ARRA", False), ("Q", True)]
    )
    def test_is_palindrome(self, s, expected):
        self.assertEqual(pl.is_palindrome(s), expected)
