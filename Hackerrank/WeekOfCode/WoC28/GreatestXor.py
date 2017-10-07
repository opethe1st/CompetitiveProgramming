#Question - https://www.hackerrank.com/contests/w28/challenges/the-great-xor
"""
a^x>x for 0<a<x 
"""
from math import log

q = int(raw_input().strip())
for a0 in xrange(q):
    x = long(raw_input().strip())
    # your code goes here
    print 2**(int(log(x,2))+1) -x-1