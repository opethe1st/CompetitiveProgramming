"""
Week of Code 25. Betweeen 2 sets - https://www.hackerrank.com/contests/w25/challenges/between-two-sets/copy-from/7581136
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
from functools import reduce
from fractions import gcd
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
def primeDecomposition(n):
    listprimes = primeslessthan(int(math.sqrt(n))+1)
    #print listprimes
    primefactorization = {}
    for a in listprimes:
        if a >n:
            break
        while n%a == 0:
            primefactorization[a] = primefactorization.get(a,0)+1
            n/=a
        if n==1:
            break
    if n>1:
        primefactorization[n] = 1
    return primefactorization

def numFactors(n):
    primefactors = primeDecomposition(n)
    res =1
    for k in primefactors:
        res*=(primefactors[k]+1)
    return res
print primeslessthan(100) 
n,m = map(int,raw_input().split())

A = map(int,raw_input().split())
B = map(int,raw_input().split())

def lcm(a,b):
    return a*b/gcd(a,b)


lcmA = reduce(lcm,A)
gcdB = reduce (gcd,B)
#print lcmA,gcdB
if gcdB%lcmA==0 and gcdB>=lcmA:
    print numFactors(gcdB/lcmA)
else:
    print 0
