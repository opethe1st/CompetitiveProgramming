def maxmex(n, k, s):
    K = k
    arr = [0]*(n+k)
    for num in s:
        if num < n+k:
            arr[num] = 1
    for i in range(n+k):
        if arr[i] == 0:
            if k > 0:
                k -= 1
                arr[i] = 1
            else:
                return i
    return n+K


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        S = map(int, input().split())
        print(maxmex(N, K, S))