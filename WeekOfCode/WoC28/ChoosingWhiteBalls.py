#It appears there is a logic error here or I have issues with precision

#!/bin/python

import sys
from fractions import Fraction
import time
start = time.time()

precomputed = {}
def remove(n,i):
    return ( ((n & (~( (1<<(i))-1 )))>>1) + (n & ( (1<<(i-1))-1)))

def score(s,n,k):
    #print 's',s,'s'
    #print
    if (s,n,k) in precomputed:
        return precomputed[(s,n,k)]
    if k==0:
        return 0
    else:
        countW = 0.0
        probability = 0.0
        
        for i in xrange(n):
            if s&(1<<i) | s&(1<<(n-i-1)):
                countW+=1
            if not(s&(1<<i) ^ s&(1<<(n-i-1))):
                probability+=max(score(remove(s,i+1),n-1,k-1)*(1.0/n), score(remove(s,n-i),n-1,k-1)*(1.0/n))
            elif s&(1<<i):
                probability+=score(remove(s,i+1),n-1,k-1)*(1.0/n)
            else:
                probability+=score(remove(s,n-i),n-1,k-1)*(1.0/n)
        probability+=(countW/n)
        precomputed[(s,n,k)] = probability
        return probability

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
balls = raw_input().strip()
# your code goes here
binballs = ['0' if v=='B' else '1' for v in balls]
binballs = 0
for v in (balls):
    binballs<<=1
    if v=='W':
        binballs+=1
#print balls,bin(binballs)
print "%.7f"%(score(binballs,n,k))
#print time.time()-start
