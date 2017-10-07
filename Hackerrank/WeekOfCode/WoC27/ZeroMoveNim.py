#Week of Code 27 - https://www.hackerrank.com/contests/w27/challenges/zero-move-nim

#!/bin/python
""" 
This solution is based on Grundy numbers. This link was useful - http://letuskode.blogspot.com.ng/2014/08/grundy-numbers.html 
I finally understand! The answer is the xor of the Grundy numbers for each pile. Given the problem description and by 
calculating the Grundy values by hand, (see the link) you can see that for an even number,a, the grundy number is a-1
and for an odd number,a, the grundy number is a+1
"""

import sys
from functools import reduce
def nimsum(piles):
    return reduce(lambda x,y: (x)^(y), piles)


g = int(raw_input().strip())
for a0 in xrange(g):
    n = int(raw_input().strip())
    p = map(int,raw_input().strip().split(' '))
    # your code goes here
    if nimsum([a-1 if a%2==0 else a+1 for a in p])==0:
        print "L"
    else:
        print "W"
    
    
