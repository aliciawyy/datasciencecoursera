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
            return min(x, y)
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

    This cannot solve complex case like the one in the test case, when same
    char repeats before the next common substring letter.
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


def is_palindrome(s):
    n_s = len(s)
    if n_s % 2 == 1:
        middle = int((n_s - 1) / 2)
        return s[:middle] == s[:middle:-1]
    return False


def get_min_palindrome(a, b):
    if len(a) == len(b):
        return min(a, b)
    else:
        return min(a, b, key=len)


def shortest_palindromes(base):
    if len(base) <= 1:
        return base
    if is_palindrome(base):
        return base
    if base[0] == base[-1]:
        return base[0] + shortest_palindromes(base[1:-1]) + base[0]
    else:
        palindrome0 = base[0] + shortest_palindromes(base[1:]) + base[0]
        palindrome1 = base[-1] + shortest_palindromes(base[:-1]) + base[-1]
        return get_min_palindrome(palindrome0, palindrome1)
