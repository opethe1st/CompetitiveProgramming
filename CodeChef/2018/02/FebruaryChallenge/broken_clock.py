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

def sqrt(x):
    ans = pow(x, ((mod+1)//4), mod)
    if pow(ans, 2, mod) != x:
        return 0
    return ans


def solution(I, D, T):
    cos_cache = {}
    sin_cache = {}
    count = 0
    cos_cache[1] = (D * inverse(I)) % mod
    sin_square = (1 - pow(cos_cache[1], 2, mod))%mod
    sin_cache[1] = sqrt(x=sin_square) if sin_square else 1
    multiplier = 1 - pow(cos_cache[1], 2, mod) if not(sin_square) else 1
    def cos(t):
        nonlocal count
        count+=1
        if t in cos_cache:
            return cos_cache[t]
        else:
            cos_cache[t] = (2*pow(cos(t//2), 2, mod) - 1)%mod if t%2 == 0 else (cos(t-t//2)*cos(t//2) - sin(t-t//2)*sin(t//2)*multiplier)%mod
            return cos_cache[t]

    def sin(t):
        nonlocal count
        count+=1
        if t in sin_cache:
            return sin_cache[t]
        else:
            sin_cache[t] = (2*sin(t//2)*cos(t//2))%mod if t%2 == 0 else (sin(t-t//2)*cos(t//2) + cos(t-t//2)*sin(t//2))%mod
            return sin_cache[t]
    ans = (cos(t=T)*I)%mod
    # print('', count)
    return ans


T = int(input())

for _ in range(T):
    I, D, T = map(int, input().split())
    print(solution(I=I, D=D, T=T))
