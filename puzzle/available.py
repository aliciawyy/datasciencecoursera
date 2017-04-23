

def read_line_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


class BAvailable(object):
    def __init__(self, n_nights, n_prices, info):
        self.n_nights = n_nights
        self.n_prices = n_prices
        self.info = info

        self.min_prices_ = self.construct_min_prices()

    def construct_min_prices(self):
        prices, min_stay, max_stay = self.info

        def get_price_wrap(k):
            nights = k + 1

            def get_price(p):
                if p[0] == 0 or nights < p[1] or nights > p[2]:
                    return p[3]
                else:
                    return p[0] if p[3] is None else min(p[0], p[3])

            current_min_price = [None] * self.n_nights
            for j in range(self.n_prices):
                current_min_price = map(
                    get_price, zip(prices[j], min_stay[j], max_stay[j],
                                   current_min_price)
                )
            min_price_start = [
                -1 if any(x is None for x in current_min_price[i:i+nights])
                else sum(current_min_price[i:i+nights])
                for i in range(self.n_nights - k)
                ]
            return min_price_start

        return map(get_price_wrap, range(self.n_nights))

    def get_total_min_price(self, start, nights):
        return self.min_prices_[nights - 1][start - 1]


N, M, Q = read_line_to_list()
INFO = [None] * 3
for i0 in range(3):
    INFO[i0] = [read_line_to_list() for _ in range(M)]

avail = BAvailable(N, M, INFO)

# print avail.get_total_min_price(6, 2)
# print avail.min_price_by_night_
# print avail.get_min_price(0, 1)


def print_query(_):
    print avail.get_total_min_price(*read_line_to_list())

map(print_query, range(Q))

# print avail.min_price_by_night_

