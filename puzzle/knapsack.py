# python knapsack.py < data/knapsack0.in


def read_line_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


def get_max_sum(arr, expected):
    arr = sorted(arr)
    all_sums = [True] + [False] * expected
    if expected < arr[0]:
        return 0
    for i in range(1, expected + 1):
        all_sums[i] = any(all_sums[i - j] for j in arr if i >= j)
    for i in range(expected, 0, -1):
        if all_sums[i]:
            return i


def solve():
    num_tests = int(raw_input())
    for _ in range(num_tests):
        _, expected = read_line_to_list()
        arr = read_line_to_list()
        print get_max_sum(arr, expected)

solve()
