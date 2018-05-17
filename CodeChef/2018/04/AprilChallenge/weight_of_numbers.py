def solution(N, W):
    if 0 <= W < 9:
        return (9-W)*pow(10, N-2, 1000000007)
    else:
        return 0

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    print(solution(N, W) % 1000000007)
