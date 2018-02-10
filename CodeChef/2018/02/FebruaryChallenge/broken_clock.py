import sys
sys.setrecursionlimit = 1000000
mod = 1000000007
# mod = 107

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def inverse(a):
    g, x, y = egcd(a, mod)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % mod


def solution(I, D, T):
    count = 0
    cos_cache = {}

    cos_cache[1] = (D * inverse(I)) % mod
    def cos(t):
        nonlocal count
        if t in cos_cache:
            return cos_cache[t]
        else:
            count += 1
            c = cos(t//2)
            cos_cache[t] = (2*pow(c, 2, mod) - 1)%mod if t%2 == 0 else (2*cos(t-1)*cos(1) - cos(t-2))%mod
            return cos_cache[t]
    # p = len(bin(T))-1
    # cos(t=(1<<p)-1)
    ans = (cos(t=T)*I)%mod
    print('num of computations', count)
    return ans


T = int(input())

for _ in range(T):
    I, D, T = map(int, input().split())
    print(solution(I=I, D=D, T=T))
