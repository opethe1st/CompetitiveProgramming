from useful import primeslessthan
from useful import eulertotient
import time

start = time.time()
N = 40000000
primes = primeslessthan(N)
print len(primes)
numTotientCache = {}
def numTotienChain(n):
    if n in numTotientCache:
        return numTotientCache[n]
    if n==0:
        return 0
    count = 0
    while n!=1:
        n=eulertotient(n)
        count +=1
    numTotientCache[n]=count+1
    return count+1

print numTotienChain(7)
print numTotienChain(18)
s = 0
for p in primes:
    if numTotienChain(p)==25:
        s+=p
        #print p
print s
print time.time()-start