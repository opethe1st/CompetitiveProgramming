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
    return ans if x**2 else 0
# print(mod%4, mod//4)
n = -1
print(n, sqrt(n), pow(sqrt(n), 2, mod))
# assert(n == pow(sqrt(n), 2, mod))

def solution(I, D, T):
    cos_cache = {}
    sin_cache = {}
    count = 0
    cos_cache[1] = (D * inverse(I)) % mod
    def cos(t):
        nonlocal count
        count+=1
        if t in cos_cache:
            return cos_cache[t]
        else:
            cos_cache[t] = (2*pow(cos(t//2), 2, mod) - 1)%mod if t%2 == 0 else 2*(cos(t-1)*cos(1) - sin(t-1)*sin(1))%mod
            return cos_cache[t]
    sin_square = (1 - pow(cos_cache[1], 2, mod))
    sin_cache[1] = sqrt(x=sin_square) # how to know which quadrant?
    def sin(t):
        nonlocal count
        count+=1
        if t in sin_cache:
            return sin_cache[t]
        else:
            sin_cache[t] = (2*sin(t//2)*cos(t//2))%mod if t%2 == 0 else (sin(t-1)*cos(1) + cos(t-1)*sin(1))%mod
            return sin_cache[t]
    ans = (cos(t=T)*I)%mod
    # print('', count)
    return ans


T = int(input())

for _ in range(T):
    I, D, T = map(int, input().split())
    print(solution(I=I, D=D, T=T))
