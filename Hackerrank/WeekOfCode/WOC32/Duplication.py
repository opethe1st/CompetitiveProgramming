#!/bin/python

import sys

def invert(s):
    invs=""
    for a in s:
        if a=='1':
            invs+='0'
        else:
            invs+='1'
    return invs
def duplication(x):
    # Complete this function
    ans = '0'
    while len(ans)<1000:
        ans=ans+invert(ans)
    return ans[x]

q = int(raw_input().strip())
for a0 in xrange(q):
    x = int(raw_input().strip())
    result = duplication(x)
    print(result)