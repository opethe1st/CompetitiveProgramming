def solution(N, M, X, K, S):
    months_left = M
    patents_left = N
    parity = 1
    available_workers = [S.count('O'), S.count('E')]
    while months_left and patents_left:
        months_left -= 1
        parity = 1 - parity
        patents_done = min(available_workers[parity], X)
        available_workers[parity] -= patents_done
        patents_left -= patents_done
    if patents_left <= 0:
        return "yes"
    else:
        return "no"


T = int(input())

for _ in range(T):
    N, M, X, K = map(int, input().split())
    S = input()
    print(solution(N=N, M=M, X=X, K=K, S=S))

