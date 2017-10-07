def solution(n):
    arr = range(1, n+1)
    for i in xrange(n-1):
        if arr[i] == (i+1):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    if arr[n-1] == (n):
            arr[n-1], arr[n-2] = arr[n-2], arr[n-1]
    return " ".join(map(str, arr))

T = input()
for _ in range(T):
    N = input()
    print(solution(N))