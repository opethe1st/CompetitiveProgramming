from itertools import combinations
from useful import is_prime
import time

start =time.time()
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
primes = primeslessthan(50000)
setprimes =set(primes)
print len(primes)
def isNotPrime(a,b):
    newnum = str(a)+str(b)
    #print newnum
    if not is_prime(int(newnum)):
        #print 'here'
        return True
    newnum= str(b)+str(a)
    if not is_prime(int(newnum)):
        return True
    return False
#print isNotPrime(109,673)
minisum = float('inf')
#print primes[4000]

primepairs = set()
for a in xrange(len(primes[:3000])):
    #print 'here',primes[a]
    for b in xrange(a):
        if isNotPrime(primes[a],primes[b]):
            continue
        else:
            primepairs.add((primes[a],primes[b]))
            primepairs.add((primes[b],primes[a]))
print 'lenprimepairs',len(primepairs)
for a in xrange(len(primes[:3000])):
    for b in xrange(a):
        if (primes[a],primes[b]) not in primepairs:
            continue
        for c in xrange(b):
            if (primes[a],primes[c]) not in primepairs or (primes[b],primes[c]) not in primepairs:
                continue
            for d in xrange(c):
                if (primes[a],primes[d]) not in primepairs or (primes[b],primes[d]) not in primepairs or (primes[c],primes[d]) not in primepairs:
                    continue
                for e in xrange(d):
                    if (primes[a],primes[e]) not in primepairs or (primes[b],primes[e]) not in primepairs or (primes[c],primes[e]) not in primepairs or (primes[d],primes[e]) not in primepairs:
                        continue
                    else:
                        print primes[a],primes[b],primes[c],primes[d],primes[e]
                        minisum = min(minisum,primes[a]+primes[b]+primes[c]+primes[d]+primes[e])
print minisum
print time.time()-start
