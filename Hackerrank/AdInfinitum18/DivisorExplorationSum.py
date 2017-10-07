#!/bin/python

import sys
Modulo = int(10**9 + 7)
# print Modulo


def primeslessthan(n):
    if n == 1:
        return []

    nums = [1] * n
    listofprimes = []
    nums[0] = nums[1] = 0
    i = 2
    while i * i < n:
        if nums[i] is 1:
            listofprimes.append(i)
            ti = i * i
            a = n - ti
            b = i
            nm = int(a / b + int(a % b > 0))
            nums[ti::i] = [0] * nm
        i = i + 1
    for b in range(i, n):
        if nums[b] is 1:
            listofprimes.append(b)
    return listofprimes


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


primes = primeslessthan(100000)
# print len(primes)
D = 2500
K = 2500
dp = [[0 for i in xrange(K + 1)] for j in xrange(D)]
dp[0][0] = 1
for j in xrange(1, D):
    dp[j][0] = 1
    for i in xrange(1, K + 1):
        dp[j][i] = dp[j][i - 1] + dp[j - 1][i]


def divisorSumPrime(p, k, d):
    ans = 0
    for i in xrange(k + 1):
        ans *= p
        ans += dp[d][i]
    # print p, k, d, ans
    return ans
# print divisorSumPrime(3, 1, 4)


def divisorExploration(m, a, d):
    res = 1
    p = primes[:m]
    e = [a + i for i in xrange(1, m + 1)]
    for i in xrange(m):
        res *= divisorSumPrime(p[i], e[i], d - 1)
        # print 'res', res, p[i], e[i], d-1
    return res


q = int(raw_input().strip())
for a0 in xrange(q):
    m, a, d = raw_input().strip().split(' ')
    m, a, d = [int(m), int(a), int(d)]
    result = divisorExploration(m, a, d) % Modulo
    print(result)
