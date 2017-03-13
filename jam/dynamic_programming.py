"""
- https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
get_flower_order

- https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
longest_zig_zag
"""


def get_flower_order(height, bloom, wilt):
    # Sort the flowers to make the height in ascending order
    flowers = sorted(zip(height, bloom, wilt))

    def is_overlap(f1, f2):
        # There is overlap when start1 <= end2 and start2 <= end1
        return f1[1] <= f2[2] and f2[1] <= f1[2]

    ordered = []
    for i, f in enumerate(flowers):
        pos = i
        # All the flowers are ordered before i
        while pos > 0 and not is_overlap(f, ordered[pos - 1]):
            pos -= 1
        ordered.insert(pos, f)
    result = [f[0] for f in ordered]
    return result


def longest_zig_zag_dp(seq):
    """
    The complexity is n2 with DP.
    """
    def to_sign(first, second):
        if first < second:
            return -1
        if first > second:
            return 1
        else:
            return 0

    n = len(seq)
    if n <= 2:
        return n

    longest_len = [0] * n
    longest_len[0] = 1
    longest_len[1] = 2
    last_diff_sign = [-1] * n
    last_diff_sign[1] = to_sign(seq[0], seq[1])
    for i, item in enumerate(seq[2:], 2):
        max_len = 0
        for j in range(i):
            current_sign = to_sign(seq[j], item)
            if last_diff_sign[j] * current_sign == -1:
                if longest_len[j] + 1 > max_len:
                    max_len = longest_len[j] + 1
                    last_diff_sign[i] = current_sign
        longest_len[i] = max_len
    return max(longest_len)


def longest_zig_zag_flat(seq):
    """
    There should be a better way to count the longest zigzag.
    """
    pass






