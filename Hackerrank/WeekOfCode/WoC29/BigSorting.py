#!/bin/python

import sys
def compare(s,t):
    if len(s)>len(t):
        return 1
    elif len(s)<len(t):
        return -1
    else:
        for i in xrange(len(s)):
            if s[i]==t[i]:
                continue
            elif s[i]>t[i]:
                return 1
            elif s[i]<t[i]:
                return -1
        return 0
            
            
            

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
# your code goes here
sortednumber = sorted(unsorted,cmp = compare)
for number in sortednumber:
    print number