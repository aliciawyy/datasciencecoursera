import collections


def read_line_to_list(as_type=int):
    lst = raw_input().strip().split(' ')
    if as_type is None:
        return lst
    return map(as_type, lst)


class TripPlanner(object):
    hours_per_day = 8

    def __init__(self, budget, price_per_day, num_attr, attractions):
        self.budget = budget
        self.price_per_day = price_per_day
        self.num_attractions = num_attr
        self.attractions = attractions

    def max_score_sum(self):
        max_sum = collections.defaultdict(int)
        max_sum[(self.budget, 0)] = 0

        max_sum_of_all = 0
        for cost, visit_time, score in self.attractions:
            new_max_sum = {}
            # print "\n", max_sum
            for (budget, time_cnt), score_sum in max_sum.items():
                day_cnt, past_time = divmod(time_cnt, self.hours_per_day)
                remaining_budget = budget - cost
                if past_time == 0 or visit_time > self.hours_per_day - past_time:
                    remaining_budget -= self.price_per_day

                if remaining_budget < 0:
                    continue
                new_key = (remaining_budget, time_cnt + visit_time)
                this_max_sum = max(max_sum[new_key], score_sum + score)
                new_max_sum[new_key] = this_max_sum
                max_sum_of_all = max(max_sum_of_all, this_max_sum)
            max_sum.update(new_max_sum)
        return max_sum_of_all


B, P, N = read_line_to_list()
ATTR = [map(int, read_line_to_list(None)[1:]) for _ in range(N)]

planner = TripPlanner(B, P, N, ATTR)
print planner.max_score_sum()
