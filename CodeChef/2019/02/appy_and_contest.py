from fractions import gcd


def solution(n, a, b, k):
    no_solved = (
        + (n // a)
        + (n // b)
        - 2 * (n * gcd(a, b) // (a * b))
    )
    return no_solved >= k


if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, A, B, K = map(int, input().split())
        if solution(n=N, a=A, b=B, k=K):
            print('Win')
        else:
            print('Lose')
