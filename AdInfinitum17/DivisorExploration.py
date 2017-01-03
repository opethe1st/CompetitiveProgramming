#!/bin/python
#https://www.hackerrank.com/contests/infinitum17/challenges/divisor-exploration-2
"""
You can find an explanation in the editorial. Not sure I can do a better job in the comments here
"""
import sys
import math
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
            nm = a/b +int(a%b>0)
            nums[ti::i] = [0]*nm
        i = i+1
    for b in xrange(i,n):
        if nums[b] is 1:
            listofprimes.append(b)

    return listofprimes

primes = primeslessthan(5000001)
#print len(primes)
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m
def modular(a):
    return modinv(a,1000000007)
invprimes = map(modular,[p-1 for p in primes])
#for i in xrange(100):
#    print (invprimes[i]*primes[i])%1000000007
q = int(raw_input().strip())
for a0 in xrange(q):
    m,a = map(int,raw_input().split())
    # your code goes here
    res = 1
    i=1
    for p in primes[:m]:
        res*=((((pow(p,a+i+2,1000000007)-1)*invprimes[i-1])-(a+i+2))*invprimes[i-1])%%1000000007
        res%=1000000007
        i+=1
    print res%1000000007