#!/bin/python

import sys

def binarySearchLE(A,x):
    if x<0:
        return -1
    #print A,x
    maxi = len(A)-1
    mini = 0
    while(mini<=maxi):
        #print mini,maxi
        mid = (mini+maxi)/2
        if A[mid]<=x:
            mini = mid+1
        elif A[mid]>x:
            maxi = mid-1
        else:
            return mid
    if maxi<0:
        return 0
    elif mini>len(A)-1:
        #print len(A)-1
        return len(A)-1
    else:
        if (mini<maxi):
            #print 'here',A[mini-1]
            return mini
        else:
            #print A[maxi]
            return maxi
g = int(raw_input().strip())
for a0 in xrange(g):
    n,m,x = raw_input().strip().split(' ')
    n,m,x = [int(n),int(m),int(x)]
    a = map(int, raw_input().strip().split(' '))
    b = map(int, raw_input().strip().split(' '))
    # your code goes here
    #print "here"
    prefixSumA = [0]*(n+1)
    for i in xrange(n):
        prefixSumA[i+1]=prefixSumA[i]+a[i]
    prefixSumB = [0]*(m+1)
    for i in xrange(m):
        prefixSumB[i+1]=prefixSumB[i]+b[i]
    #print prefixSumA,prefixSumB
    maxi=0
    for i in xrange(n+1):
        j = binarySearchLE(prefixSumB,x-prefixSumA[i])
        if j>-1:
            if (i+j)>maxi:
                maxi = i+j
    print maxi
