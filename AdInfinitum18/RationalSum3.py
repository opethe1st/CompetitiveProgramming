from fractions import Fraction
Modulo = int(10**9 + 7)


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(
            lastremainder, remainder)
        x, lastx = lastx - quotient * x, x
        y, lasty = lasty - quotient * y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)


def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def f(poly, i, x):
    poly = set(poly)
    poly.remove(a[i])
    poly.remove(a[i + 1])
    ans = 1
    for root in poly:
        ans *= (root + x)
        ans %= Modulo
    return ans


def P(poly, x):
    ans = 0
    for i in xrange(len(poly)):
        ans *= x
        ans += poly[-1 - i]
        ans %= Modulo
    return ans
# print P()


def getC(a, b):
    c = [0] * (len(a) - 1)
    c[0] = P(b, -a[0]) * modinv(f(a, 0, -a[0]), Modulo)

    for i in xrange(1, n - 2):
        c[i] = P(b, -a[i]) - c[i - 1] * (f(a, i - 1, -a[i]), Modulo)
        c[i] *= modinv(f(a, i, -a[i]), Modulo)
    c[n - 2] = P(b, -a[n - 1]) * modinv(f(a, n - 2, -a[n - 1]), Modulo)
    return c


def solution(c, a):
    ans = 0
    for i in xrange(len(c)):
        val = 0
        mina = min(a[i], a[i + 1])
        maxa = max(a[i], a[i + 1])
        for x in xrange(mina + 1, maxa + 1):
            val += 1 / Fraction(x)
        val *= c[i] / Fraction(maxa - mina)
        # print val
        ans += val
    return ans


def rationalSums(n, a, b):
    a.sort()
    c = getC(a, b)
    ans = solution(c, a)
    return ans.numerator * modinv(ans.denominator, Modulo)


n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
b = map(int, raw_input().strip().split(' '))
result = rationalSums(n, a, b) % Modulo
print(result)
