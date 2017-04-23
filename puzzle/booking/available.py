

def read_line_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


class BAvailable(object):
    def __init__(self, n_nights, n_prices, info):
        self.n_nights = n_nights
        self.n_prices = n_prices
        self.info = info

        self.min_prices_ = self.construct_min_prices()

    def construct_min_prices(self):
        zipped_info = [zip(self.info[0][j], self.info[1][j], self.info[2][j])
                       for j in range(self.n_prices)]

        def get_price_wrap(k):
            nights = k + 1

            def get_price(q):
                p, prev_price = q
                if p[0] == 0 or nights < p[1] or nights > p[2]:
                    return prev_price
                else:
                    return p[0] if prev_price is None else \
                        min(p[0], prev_price)

            current_min_price = [None] * self.n_nights
            for info in zipped_info:
                current_min_price = map(
                    get_price, zip(info, current_min_price)
                )
            min_price_start = [None] + [
                -1 if None in current_min_price[i:i+nights]
                else sum(current_min_price[i:i+nights])
                for i in range(self.n_nights - k)
                ]
            return min_price_start

        return [None] + map(get_price_wrap, range(self.n_nights))


N, M, Q = read_line_to_list()
INFO = [[read_line_to_list() for _ in range(M)] for i0 in range(3)]

avail = BAvailable(N, M, INFO)

# print avail.get_total_min_price(6, 2)
# print avail.min_price_by_night_
# print avail.get_min_price(0, 1)


def print_query(_):
    start, nights = read_line_to_list()
    print avail.min_prices_[nights][start]

map(print_query, range(Q))

# print avail.min_price_by_night_

