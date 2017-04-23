#!/bin/python


def get_ways(squares, d, m):
    cnt = 0
    for i in range(m, len(squares) + 1):
        if sum(squares[i - m:i]) == d:
            cnt += 1
    return cnt


def solve():
    _ = int(raw_input().strip())
    s = map(int, raw_input().strip().split(' '))
    d, m = map(int, raw_input().strip().split(' '))
    result = get_ways(s, d, m)
    print(result)


solve()
