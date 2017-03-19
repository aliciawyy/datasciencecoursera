"""
https://community.topcoder.com/stat?c=problem_statement&pm=2829&rd=5072
"""


class QuickSum(object):
    def __init__(self):
        self.numbers_ = None

    def set_numbers(self, numbers):
        self.numbers_ = [int(n) for n in numbers]

    def get_number(self, start, end):
        # start is not included
        result = 0
        factor = 1
        for i in range(end, start, -1):
            result += factor * self.numbers_[i]
            factor *= 10
        return result

    def min_sums(self, numbers, n_sum):
        self.set_numbers(numbers)
        n = len(self.numbers_)

        all_sums_cnt = [None] * n
        for i in range(n):
            # if combining all the digits till i to one number
            sums_cnt_i = {self.get_number(-1, i): 0}
            for j in range(i - 1, -1, -1):
                num_j = self.get_number(j, i)
                for sum_j, sum_j_cnt in all_sums_cnt[j].items():
                    key_sum = sum_j + num_j
                    sums_cnt_i[key_sum] = min(sums_cnt_i.get(key_sum, n),
                                              sum_j_cnt + 1)
            all_sums_cnt[i] = sums_cnt_i
        return all_sums_cnt[-1].get(n_sum, -1)
