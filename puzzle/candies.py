

class Candies(object):
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.num_ = [1] * self.n

    def go_back(self, k):
        # Ensure that the candies till k are correct
        for j in range(k - 1, -1, -1):
            if self.arr[j] > self.arr[j+1] and self.num_[j] == self.num_[j+1]:
                self.num_[j] += 1
            else:
                break

    def min_sum(self):
        arr = self.arr
        for i in range(1, self.n):
            if arr[i] > arr[i - 1]:
                self.num_[i] = self.num_[i - 1] + 1
            elif arr[i] < arr[i - 1] and self.num_[i - 1] == 1:
                self.go_back(i)
        return sum(self.num_)


def solve():
    n = int(raw_input())
    arr = [int(raw_input()) for _ in range(n)]
    candy = Candies(arr, n)
    print candy.min_sum()


solve()
