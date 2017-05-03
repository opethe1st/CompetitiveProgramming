from math import log
def M(p,q,N):
    biggestA = int(log(N)/log(p))
    maxi = 0
    for a in xrange(1,biggestA+2):
        b = int((log(N)-a*log(p))/log(q))
        if b>0 and (p**a)*(q**b)<=N and (p**a)*(q**b)>maxi :
            maxi = p**a*q**b
    return maxi

#print M(5,2,100)
from useful import primeslessthan
primes = primeslessthan(10**7)
#print len(primes)
N = 10**7
s = 0#set()
for i in xrange(len(primes)):
    for j in xrange(i):
        if primes[i]*primes[j]>N:
            break
        else:
            s+=M(primes[i],primes[j],N)
            #s.add( M(primes[i],primes[j],N) )
            #print primes[i],primes[j],M(primes[i],primes[j],N)

print s
