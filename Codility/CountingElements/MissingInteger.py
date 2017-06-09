def solution(A):
    arr = [False]*100001
    for a in A:
        if 0 < a <= 100000:
            arr[a] = True
    for i in range(1, 100001):
        if not arr[i]:
            return i
    return 100001

