from useful import primeslessthan
import time

start = time.time()
primes = primeslessthan(10**8)
setprimes = set(primes)
print len(primes)


def isprime(n):
    if n in setprimes:
        return True
    else:
        return False


# doesnt work.. it could start from any number.. or basically have a
# bigger loop
s = set()
for a in xrange(1, 100000000):
    n = 1
    while a * n**2 < 100000000:
        m = n + 1
        while a * m**2 < 100000000:
            if isprime(a * n * n - 1) and isprime(a * m * n - 1) and isprime(a * m * m - 1):
                s.add((a * n * n - 1, a * m * n - 1, a * m * m - 1))
            m += 1
        n += 1
    if a * n**2 > 100000000:
        break
print sum([a + b + c for a, b, c in s])
print time.time() - start
