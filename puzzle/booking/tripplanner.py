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

        for i, (cost, visit_time, score) in enumerate(self.attractions):
            new_max_sum = dict(max_sum)
            # print "\n", max_sum
            for (budget, time_cnt), score_sum in max_sum.items():
                remaining_budget = budget - cost
                pass_night, new_time_cnt = self._get_new_time_cnt(time_cnt,
                                                                  visit_time)
                if pass_night:
                    remaining_budget -= self.price_per_day
                    new_time_cnt %= self.hours_per_day

                if remaining_budget >= 0:
                    new_key = (remaining_budget, new_time_cnt)
                    new_max_sum[new_key] = max(new_max_sum.get(new_key, 0),
                                               score_sum + score)
            # print "\n", new_max_sum, '\n'*2
            max_sum.update(new_max_sum)
        return max(max_sum.values())

    def _get_new_time_cnt(self, time_cnt, visit_time):
        if time_cnt == 0:
            return True, visit_time
        passed_time = time_cnt + visit_time
        if passed_time <= self.hours_per_day:
            return False, passed_time
        else:
            return True, passed_time - self.hours_per_day


B, P, N = read_line_to_list()
ATTR = [read_line_to_list(start=1) for _ in range(N)]

planner = TripPlanner(B, P, N, ATTR)
print planner.max_score_sum()
