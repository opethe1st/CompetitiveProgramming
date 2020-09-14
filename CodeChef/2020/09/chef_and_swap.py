"""
Link to (question)[https://www.codechef.com/SEPT20B/problems/CHFNSWAP]
To solve this, I did the maths and came up with a way of generating
candidates. The key equation was

    n*(n+1)/2 = 2(k(k+1)/2 + d)

The idea behind this equation is to imagine we split the sequence into two
parts and then swap two numbers in different parts of the sequence. The sum of
the first part of the sequence will increase by d = x - y where x is taken
from the second sequence and y from the right.

when we solve the above equation for d we get

    d = n(n+1)/4 - k(k+1)/2

so we check through the values of k as long as d > 0 and d < n (since the
maximum difference is n-1). Once we have computed a value for d,
we find all the possible nice swaps between numbers in two different parts
of sequence whose difference is d. That is `max_start - min_start + 1`

for the case of d = zero. We need to swap between numbers in the same
part of the sequence. There are combination(k, 2) + combination(n-k, 2) ways
of doing this since every swap is valid because swaps don't change the sum.
"""

import math
from functools import lru_cache


def brute_force(n):
    numbers = list(range(1, n + 1))
    count = 0
    found = False
    for i in range(n):
        for j in range(i + 1, n):
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
def number_of_nice_swaps(n):
    if (n * (n + 1) // 2) % 2 == 1:
        return 0
    ans = 0
    y = ((n * n) + n) // 4
    k = int(math.sqrt(n * n / 2 - 1.5 * n + 0.25) + 0.5)
    d = None
    while True:
        d = y - (((k * k) + k) // 2)
        if d <= 0:
            break
        if d < n:
            min_start = max(1, k - d + 1)
            max_start = min(k + d, n) - d
            ans += max_start - min_start + 1
        k += 1

    if d == 0:
        ans += (k * (k - 1) // 2) + (n - k) * (n - k - 1) // 2
    return ans


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(number_of_nice_swaps(n))
