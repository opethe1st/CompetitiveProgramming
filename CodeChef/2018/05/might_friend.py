def solution(arr, k):
    a_arr = arr[::2]
    b_arr = arr[1::2]
    sum_a_arr = sum(a_arr)
    sum_b_arr = sum(b_arr)
    if sum_a_arr < sum_b_arr:
        return 'YES'
    a_arr.sort()
    b_arr.sort()
    for i in range(min(k, len(a_arr), len(b_arr))):
        diff = a_arr[len(a_arr)-i-1] - b_arr[i]
        sum_a_arr -= diff
        sum_b_arr += diff
        if sum_a_arr < sum_b_arr:
            return 'YES'
    return 'NO'

T = int(input())

for _ in range(T):
    N, K = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(solution(arr=arr, k=K))
