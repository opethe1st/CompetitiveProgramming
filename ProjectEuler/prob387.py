from math import sqrt
from math import log
import time 
start = time.time()
def primeslessthan(n):
    if n==1:
        return []

    nums =[1]*n
    listofprimes = []
    nums[0] =nums[1]=0
    i=2
    while i*i<n:
        if nums[i] is 1:
            listofprimes.append(i)
            ti = i*i
            a = n - ti
            b = i
            nm = int(a/b +int(a%b>0))
            nums[ti::i] = [0]*nm
        i = i+1
    for b in range(i,n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes
primeslist = primeslessthan(10000009)
primes = set(primeslessthan(10000009))
print len(primeslist)
def is_prime(n, _precision_for_huge_n=16):
    if n==1:
        return False
    if n in primes:
        return True
    else:
        for p in primeslist:
            if n%p==0:
                return False
            if p*p>n:
                return True
        return True


def harshad(n,s,d):
    if (10*n+d)%(s+d)==0:
        return True
    else:
        return False

dp= [[] for i in xrange(14)]
dp[0]=[]
dp[1]=[(1,1), (2,2), (3,3), (4,4) ,(5,5), (6,6), (7,7), (8,8), (9,9)]

for i in xrange(1,14):
    for n,s in dp[i-1]:
        for d in range(10):
            if harshad(n,s,d):
                dp[i].append((n*10+d,s+d))
#print (dp[2])
ans = []
for i in xrange(14):
    for n,s in dp[i]:
        if is_prime(n/s):
            ans.append(n)
print len(ans)
strongHarshadPrime = []
for num in ans:
    for d in xrange(10):
        if num*10+d<100000000000000 and is_prime(num*10+d):
            strongHarshadPrime.append(num*10+d)
#print strongHarshadPrime
print sum(strongHarshadPrime)
print time.time()-start
