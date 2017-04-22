from operator import itemgetter


def read_line_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


def transform_matrix(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]


class BAvailable(object):
    def __init__(self, n_nights, n_prices, info):
        self.n_nights = n_nights
        self.n_prices = n_prices
        self.info = info

        self.min_prices_ = {}

    def get_min_price(self, ind, nights):
        key = ind, nights
        if key not in self.min_prices_:
            def valid_price(p_info):
                return p_info[0] > 0 and p_info[1] <= nights <= p_info[2]
            day_info = filter(
                valid_price, zip(self.info[0][ind],
                                 self.info[1][ind],
                                 self.info[2][ind])
            )
            self.min_prices_[key] = -1 if not day_info else min(
                map(itemgetter(0), day_info)
            )
        return self.min_prices_[key]

    def get_total_min_price(self, start, nights):
        total_min_price = 0
        for ind in range(start - 1, start + nights - 1):
            min_price = self.get_min_price(ind, nights)
            if min_price < 0:
                return -1
            total_min_price += min_price
        return total_min_price


N, M, Q = read_line_to_list()
INFO = [None] * 3
for i0 in range(3):
    INFO[i0] = transform_matrix([read_line_to_list() for _ in range(M)])

avail = BAvailable(N, M, INFO)
for _ in range(Q):
    print avail.get_total_min_price(*read_line_to_list())
