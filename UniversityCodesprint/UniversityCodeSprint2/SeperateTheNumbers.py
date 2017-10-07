#!/bin/python

import sys
def beautiful(s,l):
    #print s,l
    n = int(s)
    temp =""
    while len(temp)<l:
        temp+=str(n)
        n+=1
    #print temp
    return temp
    

def isBeautiful(s):
    #print s
    l = len(s)
    for i in xrange(1,l/2+1):
        if s==beautiful(s[:i],l):
            return True,s[:i]
    else:
        return False,""

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    value, start = isBeautiful(s)
    if value:
        print "YES",start
    else:
        print "NO"
