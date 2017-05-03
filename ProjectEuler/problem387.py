
#dp[i]=[(s,k)]
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])
_known_primes = [2, 3]

def harshad(n,s,d):
    if (10*n+d)%(s+d)==0:
        return True
    else:
        return False

dp= [[] for i in xrange(14)]
dp[0]=[]
dp[1]=[ (2,2), (3,3), (4,4) ,(5,5), (6,6), (7,7), (8,8), (9,9)]

for i in xrange(1,14):
    for n,s in dp[i-1]:
        for d in range(10):
            if harshad(n,s,d):
                dp[i].append((n*10+d,s+d))
#print (dp[13])
ans = []
for i in xrange(14):
    for n,s in dp[i]:
        if is_prime(n/s):
            ans.append(n)
print len(ans)
strongHarshadPrime = []
for num in ans:
    for d in xrange(1,10,2):
        if num*10+d<10e13 and is_prime(num*10+d):
            strongHarshadPrime.append(num*10+d)
print sum(strongHarshadPrime)
