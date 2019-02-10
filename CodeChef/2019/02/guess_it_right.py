
TEN_TO_POWER_OF_9_PLUS_7 = 1_000_000_007


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m


def modinv10power9plus7(a):
    return modinv(a, TEN_TO_POWER_OF_9_PLUS_7)


def solution(N, K, M):
    NInverse = modinv10power9plus7(N)
    probabilityOfFailure = (1 - NInverse) % TEN_TO_POWER_OF_9_PLUS_7
    ans = 0
    currentMultiplier = 1
    ans = (1 - pow(probabilityOfFailure, (M - 1) // 2 + 1, TEN_TO_POWER_OF_9_PLUS_7))
    currentMultiplier = pow(probabilityOfFailure, (M - 1) // 2 + 1, TEN_TO_POWER_OF_9_PLUS_7)
    if (M % 2) == 0:
        ans += currentMultiplier * modinv10power9plus7(N + K)
    return ans % TEN_TO_POWER_OF_9_PLUS_7


T = int(input())

for _ in range(T):
    N, K, M = map(int, input().split())
    print(solution(N=N, K=K, M=M))
