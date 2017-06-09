#!/bin/python

import sys
from decimal import Decimal, getcontext,Context
from math import pi as PI

pi = Context(prec=60).create_decimal('3.1415926535897932384626433832795028841971693993751')
PI = pi
def calc(fun, n):
    temp = Decimal("0.0")
 
    for ni in xrange(n+1, 0, -1):
        (a, b) = fun(ni)
        temp = Decimal(b) / (a + temp)
 
    return fun(0)[0] + temp

def fpi(n):
    return (6 if n > 0 else 3, (2 * n - 1) ** 2)

#print "%.50f"%(calc(fpi, 1001))

#mini,maxi = raw_input().strip().split(' ')
mini,maxi = 200,231#[long(mini),long(maxi)]
# your code goes here

minifraction = (3,1)
minidecimal = Decimal(3.0)
#print PI
for d in xrange(mini,maxi+1):
    #print d
    n = int(pi*d)
    d1 = n/Decimal(d)
    d2 = (n+1)/Decimal(d)
    #print n,d,d1,d2
    if abs(d1-pi)<abs(d2-pi):
        if abs(d1-pi)<abs(minidecimal-pi):
            minifraction = (n,d)
            minidecimal = n/Decimal(d)
    if abs(d1-pi)>abs(d2-pi):
        if abs(d2-pi)<abs(minidecimal-pi):
            #print n,d,d1,d2
            minifraction = (n+1,d)
            minidecimal = (n+1)/Decimal(d)
    #print minifraction
            
print "%d/%d"%(minifraction[0],minifraction[1])
            
 
            

          
    
    
