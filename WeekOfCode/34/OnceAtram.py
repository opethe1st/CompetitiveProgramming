def sumdigits(n):
    s = 0
    while n > 0:
        s += (n % 10)
        n /= 10
    return s

#tests
assert sumdigits(0) == 0
assert sumdigits(1) == 1
assert sumdigits(199) == 19


def nextLuckyNumber(n):
    for i in xrange(n+1, 1000000):
        first = i / 1000
        second = i % 1000
        sumfirst = sumdigits(first)
        sumsecond = sumdigits(second)
        if sumfirst == sumsecond:
            return i

print nextLuckyNumber(input())