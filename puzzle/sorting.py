
def print_n(x):
    print x,


def print_arr(arr):
    map(print_n, arr)
    print ''


def print_insertion_sort(arr):
    for i in range(1, len(arr)):
        num_i = arr[i]
        k = i
        for j in range(i - 1, -1, -1):
            if num_i < arr[j]:
                print_arr(arr[:j + 1] + arr[j:i] + arr[i + 1:])
                k = j
        if k < i:
            arr = arr[:k] + arr[i:i + 1] + arr[k:i] + arr[i + 1:]
            print_arr(arr)


def print_insertion_sort2(arr):
    for i in range(1, len(arr)):
        num_i = arr[i]
        k = i
        for j in range(i - 1, -1, -1):
            if num_i < arr[j]:
                k = j
        if k < i:
            arr = arr[:k] + arr[i:i + 1] + arr[k:i] + arr[i + 1:]
        print_arr(arr)


def get_num_shift(arr):
    cnt = 0
    for i in range(1, len(arr)):
        k = i
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                k = j
                cnt += 1
        if k < i:
            arr = arr[:k] + arr[i:i + 1] + arr[k:i] + arr[i + 1:]
    return cnt


def solve():
    n = int(raw_input())
    arr = map(int, raw_input().strip().split(' '))
    # print_insertion_sort(arr)
    print get_num_shift(arr)

solve()
