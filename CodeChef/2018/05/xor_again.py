from functools import reduce

def solution(arr):
    return reduce(lambda x, y: x^y, [2*item for item in arr])

T = int(input())

for _ in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solution(arr=arr))
