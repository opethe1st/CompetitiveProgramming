from math import sqrt


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
            nm = a / b + int(a % b > 0)
            nums[ti::i] = [0] * nm
        i = i + 1
    for b in xrange(i, n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes


def primesbetween(m, n):
    n = n+1
    primes = primeslessthan(int(sqrt(n)+1))
    setprimes = set(primes)
    # print primes, m, n
    nums = [1]*(n - m)
    listofprimes = []
    for p in primes:  # go through all primes
        start = m + (p - (m % p)) % p
        if start in setprimes:
            start += p
        for i in xrange(start, n, p):
            nums[i-m] = 0
    for i in xrange(n-m):
        if nums[i] == 1 and (i+m) != 1:
            listofprimes.append(i+m)
    return listofprimes

#print primesbetween(1, 100)
#"""
T = input()
for _ in xrange(T):
    n, m = map(int, raw_input().split())
    primes = primesbetween(n, m)
    for p in primes:
        print p
    print
#"""