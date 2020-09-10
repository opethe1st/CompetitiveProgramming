"""
Sequence: (1, 2,..,n)
choose two elements of this sequence and swap them
a swap is nice if there is an integer M such that the sum of the
first M elements equals the sum of the last N-M elements
Find the number of nice swaps
Ideas
Idea

"""

import math
from functools import lru_cache


def brute_force(n):
    numbers = list(range(1, n+1))
    count = 0
    found = False
    for i in range(n):
        for j in range(i+1, n):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            found = False
            for m in range(1, n):
                if sum(numbers[:m]) == sum(numbers[m:]):
                    found = True
                    break
            if found:
                count += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    return count


@lru_cache(maxsize=None)
def solution(n):
    # print('solution n:', n)
    if (n * (n + 1) // 2) % 2 == 1:
        return 0
    ans = 0
    y = ((n * n) + n) // 4
    k = int(math.sqrt(n*n/2 -  1.5*n+ 0.25) + 0.5)
    d = None
    while True:
        d = y - (((k * k) + k) // 2)
        if d <= 0:
            break
        if d < n:
            min_start = max(1, k-d+1)
            max_start = min(k+d, n) - d
            ans += max_start - min_start + 1
        k += 1

    if d == 0:
        ans += (k * (k - 1) // 2) + (n - k) * (n - k - 1) // 2
    return ans


# for i in range(1, 20):
#     assert solution(i) == brute_force(i), (i)

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(solution(n))
