from fractions import gcd
from functools import reduce


def gcd_list(arr):
    return reduce(gcd, arr)


T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    g = gcd_list(arr=arr)
    if g == 1:
        print(0)
    else:
        print(-1)
