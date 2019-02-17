T = int(input())


for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    d = list(map(int, input().split()))
    a = [a[-1]] + a + [a[0]]
    d = [d[-1]] + d + [d[0]]

    maxd = -1
    for i in range(1, N + 1):
        # print(':', d[i], (a[i - 1] + a[i + 1]), maxd)
        if d[i] > (a[i - 1] + a[i + 1]):
            if d[i] > maxd:
                maxd = d[i]
    print(maxd)
