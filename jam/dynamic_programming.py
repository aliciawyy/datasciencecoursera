"""
- https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
get_flower_order

- https://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
longest_zig_zag

- https://community.topcoder.com/stat?c=problem_statement&pm=2402&rd=5009
max_donation_from_neighbors
"""
import numpy as np


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


def longest_zig_zag(seq):
    """
    The complexity is n2 with DP.
    Auxiliary Space is n.
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

    max_longest_len = 2
    for i, item in enumerate(seq[2:], 2):
        max_len = 0
        for j in range(i):
            current_sign = to_sign(seq[j], item)
            if last_diff_sign[j] * current_sign == -1:
                if longest_len[j] + 1 > max_len:
                    max_len = longest_len[j] + 1
                    last_diff_sign[i] = current_sign
        longest_len[i] = max_len
        max_longest_len = max(max_longest_len, max_len)
    return max_longest_len


def max_donation_from_neighbors(donations):
    # init
    dons = np.array(donations, dtype=np.int16)
    dons = np.roll(dons, -np.argmax(dons))

    first_element_in = [True] * len(dons)
    first_element_in[1] = False
    max_list = list(dons)

    max_donation = max_list[0]
    for i, donation_i in enumerate(dons[2:-1], 2):
        max_i = max_list[0] + donation_i
        for j in range(1, i - 1):
            max_j = max_list[j] + donation_i
            if max_j > max_i:
                max_i = max_j
                first_element_in[i] = first_element_in[j]
        max_list[i] = max_i
        max_donation = max(max_donation, max_i)

    last_donation = dons[-1]
    for i, don_i in enumerate(dons[1:-2]):
        if not first_element_in[i]:
            max_donation = max(max_donation, last_donation + don_i)
    return max_donation
