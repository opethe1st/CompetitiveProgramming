#!/bin/python
#https://www.hackerrank.com/contests/infinitum17/challenges/primitive-problem
"""
Check all the divisors of s = p-1. if if for a given test root , none of its primefactors gives 
pow(root,s/prime,p)==1 then it is the smallest primitive root. To count the number of primitive roots
that's equal to the eulertotient of p-1. This can be mathematically proven
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

def eulertotient(n):

    res = n
    i = 2
    while i*i<=n:
        if n%i==0:
            res -= res/i
            while n%i == 0:
                n/=i
        i+=1
    if n>1:
        res -= res/n
    return res
p = int(raw_input().strip())
# your code goes here


s = p-1
roots = []
primes = primeslessthan(1000000)

primefactors = []
for prime in primes:
    if s%prime==0:
        primefactors.append(prime)
for root in xrange(2,p):
    for prime in primefactors:
        if pow(root,s/prime,p)==1:
            break
    else:
        roots.append(root)
        break
print min(roots),eulertotient(s)  
