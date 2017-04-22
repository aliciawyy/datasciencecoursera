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
        self.process_info()
        # for i, x in enumerate(self.info, 1):
        #    print i, x

        self.min_price_by_night_ = {}

    def process_info(self):
        def valid_price(p_info):
            return p_info[0] > 0

        new_info = [None] * self.n_nights
        for ind in range(self.n_nights):
            new_info[ind] = filter(
                valid_price, zip(self.info[0][ind], self.info[1][ind],
                                 self.info[2][ind])
            )
        self.info = new_info

    def get_min_price(self, nights):
        if nights not in self.min_price_by_night_:
            def valid_price(p_info):
                return p_info[1] <= nights <= p_info[2]

            def min_price(day_info):
                v = map(itemgetter(0), filter(valid_price, day_info))
                return -1 if len(v) == 0 else min(v)

            self.min_price_by_night_[nights] = map(min_price, self.info)
        return self.min_price_by_night_[nights]

    def get_total_min_price(self, start, nights):
        min_prices = self.get_min_price(nights)
        price_in_rg = min_prices[start - 1: start + nights - 1]
        return -1 if any(p < 0 for p in price_in_rg) else sum(price_in_rg)


N, M, Q = read_line_to_list()
INFO = [None] * 3
for i0 in range(3):
    INFO[i0] = transform_matrix([read_line_to_list() for _ in range(M)])

avail = BAvailable(N, M, INFO)

# print avail.get_total_min_price(6, 2)
# print avail.min_price_by_night_
# print avail.get_min_price(0, 1)
for _ in range(Q):
    print avail.get_total_min_price(*read_line_to_list())

# print avail.min_price_by_night_

