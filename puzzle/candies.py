# python candies.py < data/candies1.in


def count_increasing(ratings, n):
    """
    Only considering the increasing case
    """
    arr = [1] * n
    cnt = 1
    for i in range(1, n):
        cnt = cnt + 1 if ratings[i - 1] < ratings[i] else 1
        arr[i] = cnt
    return arr


def min_sum(ratings, n):
    increase_cnt = count_increasing(ratings, n)
    ratings.reverse()
    decrease_cnt = count_increasing(ratings, n)
    decrease_cnt.reverse()
    return sum(map(max, zip(increase_cnt, decrease_cnt)))


def solve():
    n = int(raw_input())
    ratings = [int(raw_input()) for _ in range(n)]
    print min_sum(ratings, n)


solve()
