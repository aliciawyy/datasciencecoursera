"""
https://community.topcoder.com/stat?c=problem_statement&pm=1861&rd=4630
"""


def longest_common_sub_sequence(a, b):
    """
    http://www.geeksforgeeks.org/
    dynamic-programming-set-4-longest-common-subsequence/
    """
    def get_max(x, y):
        """
        if lengths are the same, return the lexicographically earliest
        """
        if len(x) == len(y):
            return '' if x == '' else min(x, y)
        return max(x, y, key=len)

    n_a = len(a)
    n_b = len(b)
    result = [[''] * (n_b + 1) for _ in range(n_a + 1)]
    # result[i][j] stores the longest common sub sequence of string
    # a[:i] and b[:j]
    for i in range(1, n_a + 1):
        for j in range(1, n_b + 1):
            if a[i - 1] == b[j - 1]:
                result[i][j] = result[i - 1][j - 1] + a[i - 1]
            else:
                result[i][j] = get_max(result[i - 1][j], result[i][j - 1])
    return result[-1][-1]


def sort_merge_string(x, y):
    result = ''
    while len(x) > 0 or len(y) > 0:
        if len(x) == 0:
            result += y
            y = ''
        elif len(y) == 0:
            result += x
            x = ''
        elif x[0] < y[0]:
            result += x[0]
            x = x[1:]
        else:
            result += y[0]
            y = y[1:]
    return result


def shortest_common_super_sequence(a, b):
    """
    get the shortest common string for a and b
    """
    def separate_by_char(letter, seq):
        idx_seq = seq.find(letter)
        return seq[:idx_seq], seq[idx_seq + 1:]
    common_sub_seq = longest_common_sub_sequence(a, b)
    result = ''
    for ch in common_sub_seq:
        chunk_a, a = separate_by_char(ch, a)
        chunk_b, b = separate_by_char(ch, b)
        result += ''.join(sort_merge_string(chunk_a, chunk_b)) + ch
    result += ''.join(sort_merge_string(a, b))
    return result


class ShortPalindromes(object):
    def __init__(self):
        self.base_ = None

    def set_base(self, base):
        self.base_ = base

    def shortest(self, base):
        self.set_base(base)
        min_seq = self.base_ + self.base_
        for i, ch in enumerate(self.base_):
            # get the result if putting ch in the middle
            seq = shortest_common_super_sequence(self.base_[:i],
                                                 self.base_[:i:-1])
            palindrome = seq + ch + seq[::-1]
            if len(palindrome) < len(min_seq):
                min_seq = palindrome
            elif len(palindrome) == len(min_seq) and palindrome < min_seq:
                min_seq = palindrome
        return min_seq
