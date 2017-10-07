#Best Divisor - Week of Code 26 - https://www.hackerrank.com/contests/w26/challenges/best-divisor

#!/bin/python
def sumdigits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def compare(a,b):
    sa = sumdigits(a)
    sb = sumdigits(b)
    if sa>sb:
        return True
    elif sa==sb:
        if a<b:
            return True
        else:
            return False
    else:
        return False
    


def soln(n):
    import math
    f = []
    for i in xrange(1,int(math.sqrt(n))+1):
        if n%i==0:
            f.append(i)
            f.append(n/i)
    mx = 1
    for num in f:
        if compare(num,mx):
            mx=num
    return mx
            
import sys


n = int(raw_input().strip())
print soln(n)
