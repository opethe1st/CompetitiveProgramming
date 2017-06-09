#!/bin/python

import sys
import time
start = time.time()
def geometricTrick(s):
    # Complete this function
    myset = set()
    for k in range(1,n/4+2):
        x=1
        while k*x*x<=n:
            #print k*x*x,k*(x+1)**2,k
            y=x+1
            while k*y*y<=n:
                #print k*x**2,k*x*y,k*y**2
                if (s[k*x*x-1]=='a' and s[k*x*y-1]=='a' and s[k*y*y-1]=='a') or (s[k*x*x-1]=='c' and s[k*x*y-1]=='b' and s[k*y*y-1]=='a') :
                    myset.add((k*x*x-1,k*x*y-1,k*y*y-1))
                    #print (k*x*x-1,k*x*y-1,k*y*y-1)
                y+=1
            x+=1
    return len(myset)
n = 500000#int(raw_input().strip())
s = 'aaa'*100000+'aa'*100000#raw_input().strip()
print len(s)
result = geometricTrick(s)
print(result)
print time.time()-start
