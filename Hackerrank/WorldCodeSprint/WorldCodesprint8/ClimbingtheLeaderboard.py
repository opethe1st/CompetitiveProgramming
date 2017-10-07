#!/bin/python
#World code sprint 8
import sys


n = int(raw_input().strip())
scores = map(int,raw_input().strip().split(' '))
m = int(raw_input().strip())
alice = map(int,raw_input().strip().split(' '))
# your code goes here

scores.append(0)
scores.insert(0,float('inf'))
scores.reverse()

#scores = [0,10,20,40,40,50,100,100,float('inf')]
pos = [0]*(len(scores))

for i in reversed(xrange(1,len(scores))):
    if scores[i]>scores[i-1]:
        pos[i-1]=pos[i]+1
    else:
        pos[i-1]=pos[i]
#print scores
#print pos    

def findPos(num,start,end):
    
    mid = (start+end)/2
    #print start,mid,end,scores[start],scores[end],scores[mid],scores[mid+1]
    if scores[mid-1]<=num<scores[mid]:
        return pos[mid]
    elif scores[mid]<=num<scores[mid+1]:
        return pos[mid+1]
    elif scores[mid]<=num:
        return findPos(num,mid,end)
    elif scores[mid-1]>num:
        return findPos(num,start,mid)
    else:
        return "error"

for s in alice:
    print findPos(s,0,len(scores)-1)+1 

