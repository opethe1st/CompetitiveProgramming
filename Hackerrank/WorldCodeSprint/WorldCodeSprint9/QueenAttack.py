#!/bin/python
#https://www.hackerrank.com/contests/world-codesprint-9/challenges/queens-attack-2s
import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
rQueen,cQueen = [int(rQueen),int(cQueen)]
obstacles = []
for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    Obstacle = [int(rObstacle),int(cObstacle)]
    # your code goes here
    obstacles.append(Obstacle)

class1,class2,class3,class4,class5,class6,class7,class8=rQueen-1,n-rQueen,cQueen-1,n-cQueen,min(rQueen-1,cQueen-1),min(n-rQueen,n-cQueen),min(rQueen-1,n-cQueen),min(n-rQueen,cQueen-1)
#print class1,class2,class4,class5,class6,class7,class8
for x,y in obstacles:
    if rQueen==x:
        if y<cQueen:
            class1=min(class1,cQueen-y-1)
        else:
            class2=min(class2,y-cQueen-1)
    elif cQueen==y:
        if x<rQueen:
            class3=min(class3,rQueen-x-1)
        else:
            class4=min(class4,x-rQueen-1)
    elif (rQueen-x)==(cQueen-y):
        if x<rQueen:
            class5=min(class5,rQueen-x-1)
        else:
            class6=min(class6,x-rQueen-1)
    elif (rQueen-x)==(y-cQueen):
        if x<rQueen:
            class7=min(class7,rQueen-x-1)
        else:
            class8=min(class8,x-rQueen-1)
print class1,class2,class3,class4,class5,class6,class7,class8        
print class1+class2+class3+class4+class5+class6+class7+class8
    
