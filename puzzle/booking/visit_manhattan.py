import collections
from operator import itemgetter


def readlint_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


X, Y, L, H = readlint_to_list()
dimensions = [X, Y]
landmarks = [readlint_to_list() for _ in range(L)]
hotels = [readlint_to_list() for _ in range(H)]


def construct_cache(n_dim):
    grid_limit = dimensions[n_dim]
    raw_grid = map(itemgetter(n_dim), landmarks)
    current_grid = collections.Counter(raw_grid)
    L = 0
    R = sum([k * v for k, v in current_grid.items()])
    K = 0
    num = len(raw_grid)

    # R - L, coef
    cache_value = [(None, None)] * (grid_limit + 1)
    cache_value[0] = R - L, -num

    for i in range(1, grid_limit + 1):
        prev = cache_value[i - 1]
        if i not in current_grid:
            cache_value[i] = prev
        else:
            cnt = current_grid[i]
            increment = i * cnt
            L += increment
            R -= increment
            K += cnt
            cache_value[i] = R - L, 2 * K - num
    return cache_value


cache_values = map(construct_cache, range(2))


def get_sum_1d(num_dim, v):
    v0, coef = cache_values[num_dim][v]
    return v0 + coef * v


def get_sum(point):
    return get_sum_1d(0, point[0]) + get_sum_1d(1, point[1])


min_dist = 1e20
ind_hotel = -1
for i, hotel in enumerate(hotels, 1):
    score = get_sum(hotel)
    if score < min_dist:
        min_dist = score
        ind_hotel = i

print ind_hotel
