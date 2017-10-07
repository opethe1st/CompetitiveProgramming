#Week of Code 27 - https://www.hackerrank.com/contests/w27/challenges/how-many-substrings/
"""
Very Naive brute force solution.. :) Obviously not good enough
"""
#!/bin/python

import sys

d = {}
def countSubString(s):
    #print s
    if s in d:
        return d[s]
    sset = set()
    for i in xrange(len(s)):
        for j in xrange(i+1,len(s)+1):
            sset.add(s[i:j])
    d[s]=len(sset)
    return d[s]

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
s = raw_input().strip()
for a0 in xrange(q):
    left,right = raw_input().strip().split(' ')
    left,right = [int(left),int(right)]
    # your code goes here
    print countSubString(s[left:right+1])
