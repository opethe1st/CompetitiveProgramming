#Week of Code 27 - day 3 - https://www.hackerrank.com/contests/w27/challenges/hackonacci-matrix-rotations
import time
import sys

start=time.time()

# input
n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]

#initial hackonacci values for odd and even values. 1 for odd, 0 for even.
hackonacci=1,1,0,1,0,0,1
#there is a pattern and the polarity of the remaining hackonacci values can be calculated from hackonacci[n]=hackonacci[n%7]
#calculate a few values to see how this is true. In general, hackonacci[n]=hackonacci[n-1]+2*hackonacci[n-2]+3*hackonacci[n-3]

#Build the hackonacci matrix
hackonacciMatrix = [[0 for i in xrange(n)] for j in xrange(n)]
for i in xrange(n):
    for j in xrange(n):
        hackonacciMatrix[i][j]=hackonacci[((i+1)*(j+1))**2%7]

#nDiffOriginalRotated[i] is the number of different elements between the original and matrix when it is rotated i times
nDiffOriginalRotated = [0]*4

#for rotation of 90
for i in xrange(n):
    for j in xrange(n):
        if hackonacciMatrix[i][j]!=hackonacciMatrix[i][n-1-j]:
            nDiffOriginalRotated[1]+=1
#for rotation of 180
for i in xrange(n):
    for j in xrange(n):
        if hackonacciMatrix[i][j]!=hackonacciMatrix[n-i-1][n-1-j]:
            nDiffOriginalRotated[2]+=1
#for rotation of 270
for i in xrange(n):
    for j in xrange(n):
        if hackonacciMatrix[n-i-1][j]!=hackonacciMatrix[i][j]:
            nDiffOriginalRotated[3]+=1


for a0 in xrange(100000):
    angle = int(raw_input().strip())
    #angle = angle%360 and angle/90 gives the number of rotations
    nDiffOriginalRotated[(angle%360)/90]
print time.time()-start
