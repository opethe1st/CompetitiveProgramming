from useful import primeslessthan
import time
from math import floor

start = time.time()
N = 10**8
MOD = 1000000009
primes = primeslessthan(N)
print "here"
def primedecompNFactorial(n):
    #100 000 000
    pf ={}
    #primes = primeslessthan(n)
    for p in primes:
        power = p
        while power<=n:
            pf[p] = pf.get(p,0)+n/power
            power *= p
    return pf
#print len(primedecompNFactorial(N))
def sumSquareUnitaryDivisors(n):
    pf = primedecompNFactorial(n)
    #print pf
    ans = 1
    fact = 1
    for p in pf:
        pp =1+ pow(p,2*pf[p],MOD )
        ans*=pp
        #fact=fact*pp
        ans%=MOD
    #print ans,fact+1
    #ans+=(fact+1)
    return ans%MOD

print sumSquareUnitaryDivisors(N)
print sumSquareUnitaryDivisors(4)
print time.time()-start