T = int(input())
for _ in range(T):
    n = input()
    p = list(map(int, input().split()))
    print(
        sum(
            [abs(abs(x-y) - 1) for x, y in zip(p, p[1:])]
        )
    )
