def solution(N, A, C, D, S):
    return (C-1)*sum(A)

T = int(input())

for _ in range(T):
    N = int(input())
    A = map(int, input().split())
    C, D, S = map(int, input().split())
    print(solution(N=N, A=A, C=C, D=D, S=S))

