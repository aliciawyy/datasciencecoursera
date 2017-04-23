def read_line_to_list(as_type=int, start=0):
    lst = raw_input().strip().split(' ')
    if start > 0:
        lst = lst[start:]
    return map(as_type, lst)


class TripPlanner(object):
    hours_per_day = 8

    def __init__(self, budget, price_per_day, num_attr, attractions):
        self.budget = budget
        self.price_per_day = price_per_day
        self.num_attractions = num_attr
        self.attractions = attractions

    def max_score_sum(self):
        max_sum = {(self.budget, 0): 0}

        for cost, visit_time, score in self.attractions:
            new_max_sum = dict(max_sum)
            # print "\n", max_sum
            for (budget, time_cnt), score_sum in max_sum.items():
                past_time = time_cnt % self.hours_per_day
                remaining_budget = budget - cost
                if past_time == 0 or visit_time > self.hours_per_day - past_time:
                    remaining_budget -= self.price_per_day

                if remaining_budget >= 0:
                    new_key = (remaining_budget, time_cnt + visit_time)
                    new_max_sum[new_key] = max(new_max_sum[new_key],
                                               score_sum + score)
            max_sum.update(new_max_sum)
        return max(max_sum.values())


B, P, N = read_line_to_list()
ATTR = [read_line_to_list(start=1) for _ in range(N)]

planner = TripPlanner(B, P, N, ATTR)
print planner.max_score_sum()
