

class Candies(object):
    def __init__(self, arr, n):
        self.arr = arr
        self.n = n
        self.num_ = [1] * self.n
        # If j-th item is True, it means rating from j - 1 to j is decreasing
        self.decreasing_ = [False] * self.n
        self.k_ = 1
        self._init()

    def _init(self):
        in_init_range = True
        for i in range(1, self.n):
            if self.arr[i] < self.arr[i - 1]:
                self.decreasing_[i] = True
            elif in_init_range:
                self.k_ = i
                in_init_range = False

        if in_init_range:
            self.k_ = self.n

        for i in range(0, self.k_):
            self.num_[i] = self.k_ - i

    def go_back(self, k):
        # Ensure that the candies till k are correct
        for j in range(k - 1, -1, -1):
            if self.decreasing_[j+1] and self.num_[j] == self.num_[j+1]:
                self.num_[j] += 1
            else:
                break

    def min_sum(self):
        for i in range(self.k_, self.n):
            if self.arr[i] > self.arr[i - 1]:
                self.num_[i] = self.num_[i - 1] + 1
            elif self.decreasing_[i] and self.num_[i - 1] == 1:
                self.go_back(i)
        return sum(self.num_)


def solve():
    n = int(raw_input())
    arr = [int(raw_input()) for _ in range(n)]
    candy = Candies(arr, n)
    print candy.min_sum()


solve()
