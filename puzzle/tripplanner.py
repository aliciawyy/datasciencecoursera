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
        self.attractions = [(score, -visit_time, -cost)
                            for cost, visit_time, score in attractions]
        self.attractions = sorted(self.attractions)
        for i in self.attractions:
            print i

    def max_score_sum(self):
        return self.knapsack(self.budget, 0, 0, self.num_attractions)

    def knapsack(self, budget, time_cnt, day_cnt, n):
        if n == 0 or budget == 0:
            return 0

        info = self.attractions[n - 1]
        score, visit_time, cost = info[0], -info[1], -info[2]
        pass_night = int(time_cnt + visit_time / self.hours_per_day) > day_cnt
        if pass_night:
            cost += self.price_per_day
            add_additional_day = 1
        else:
            add_additional_day = 0

        # Check if we can include the n-th attraction
        score_if_not = self.knapsack(budget, time_cnt, day_cnt, n - 1)

        if budget < cost:
            return score_if_not
        else:
            score_if_visit_current = score + self.knapsack(
                budget - cost, time_cnt + visit_time,
                day_cnt + add_additional_day,
                n - 1
            )
            return max(score_if_visit_current, score_if_not)

B, P, N = read_line_to_list()
ATTR = [map(int, read_line_to_list(None)[1:]) for _ in range(N)]

planner = TripPlanner(B, P, N, ATTR)
print planner.max_score_sum()