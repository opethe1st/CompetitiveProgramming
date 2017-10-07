#!/bin/python

import sys


def findMin2(ar1):
    """return the two index with the first being the least value and the second, 
    the second least"""
    minindex = 0
    n = len(ar1)
    for i in xrange(len(ar1)):
        if ar1[i] < ar1[minindex]:
            minindex = i
    minindex2 = (minindex + 1) % n
    for i in xrange(len(ar1) - 1):
        if ar1[(i + minindex + 1) % n] < ar1[minindex2]:
            minindex2 = (i + minindex + 1) % n
        # print 'i', i, (i + minindex + 1) % n
    return minindex, minindex2


#print findMin2([11, 6, 4, 4, 6])


def twinArrays(ar1, ar2):
    # Complete this function
    min1, min2 = findMin2(ar1)
    min3, min4 = findMin2(ar2)
    if min1 != min3:
        return ar1[min1] + ar2[min3]
    else:
        possible = []
        if min1 != min4:
            possible.append(ar1[min1]+ar2[min4])
        if min2 != min3:
            possible.append(ar1[min2]+ar2[min3])
        return min(possible)

    


n = int(raw_input().strip())
ar1 = map(int, raw_input().strip().split(' '))
ar2 = map(int, raw_input().strip().split(' '))
result = twinArrays(ar1, ar2)
print(result)
