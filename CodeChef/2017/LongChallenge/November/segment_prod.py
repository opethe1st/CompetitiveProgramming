class RangeQuery:

    def __init__(self, arr, mod):
        self.arr = arr
        self.length = len(arr)
        self.mod = mod
        self.range_arr = self._preprocess()

    def _preprocess(self):
        logn = 0
        while (1 << logn) <= self.length:
            logn += 1
        range_arr = [[-1 for j in range(logn)] for i in range(self.length)]
        for i in range(self.length):
            range_arr[i][0] = self.arr[i] #% self.mod
        j = 1
        while (1 << j) <= self.length:
            i = 0
            while (i+(1 << j) - 1) < self.length:
                range_arr[i][j] = (range_arr[i][j-1]*range_arr[i + (1 << (j-1))][j-1]) % self.mod
                i += 1
            j += 1
        return range_arr

    def product(self, left, right):
        diff = right-left
        powers = []
        j = 0
        while (1 << j) <= diff:
            if (diff >> j) & 1:
                powers.append(j)
            j += 1
        res = 1
        var = left
        for power in powers:
            res *= self.range_arr[var][power]
            var += (1 << power)
            res %= self.mod
        return res

T = int(input())

for _ in range(T):
    n, p, q = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    rq = RangeQuery(arr=A, mod=p)
    x = 0
    prel = 0
    prer = 0
    for i in range(q):
        l = min((B[i//64]+x)%n, (B[i//64+1]+x)%n) if i % 64 == 0 else min((prel+x)%n, (prer+x)%n)  # pylint: disable=line-too-long
        r = max((B[i//64]+x)%n, (B[i//64+1]+x)%n) if i % 64 == 0 else max((prel+x)%n, (prer+x)%n)  # pylint: disable=line-too-long
        x = (rq.product(l, r+1)+1)%p
        prel, prer = l, r
    print(x)
