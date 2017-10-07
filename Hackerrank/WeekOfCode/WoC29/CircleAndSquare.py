#!/bin/python

import sys
from math import sqrt

w,h = raw_input().strip().split(' ')
w,h = [int(w),int(h)]
a,b,r = map(int,raw_input().strip().split(' '))
x1,y1,x3,y3 = raw_input().strip().split(' ')
x1,y1,x3,y3 = [int(x1),int(y1),int(x3),int(y3)]
# your code goes here

display = [ ["." for x in xrange(w)] for y in xrange(h)]

#for circle
def inCircle(x,y):
    if r**2-(y-b)**2<0:
        return False
    elif a-(sqrt(r**2-(y-b)**2)) <= x <= a+(sqrt(r**2-(y-b)**2)):
        return True
    else:
        return False    
for y in xrange(h):
    for x in xrange(w):
        if inCircle(x,y):
            display[y][x]="#"
            pass

            
#For Square
x4,y4 = ((x1+x3+y3-y1)/2.0,(y1+y3+x1-x3)/2.0 )
x2,y2 = ((x1+x3+y1-y3)/2.0 , (y1+y3+x3-x1)/2.0)
#print x1,y1
#print x2,y2
#print x3,y3
#print x4,y4
def inSquare(x,y):
    if (x1-x2)==0:
        miny = min(y1,y3)
        maxy = max(y1,y3)
        minx = min(x1,x3)
        maxx = max(x1,x3)
        if minx <= x <= maxx and miny <= y <= maxy:
            return True
        else:
            return False
    else:
        miny = min((y2-y1)*(x-x1)/float(x2-x1)+y1 , (y4-y3)/float(x4-x3)*(x-x3)+y3)
        maxy = max((y2-y1)*(x-x1)/float(x2-x1)+y1 , (y4-y3)/float(x4-x3)*(x-x3)+y3)
        minx = min((x1-x4)*(y-y4)/float(y1-y4)+x4 , (x3-x2)*(y-y2)/float(y3-y2)+x2)
        maxx = max((x1-x4)*(y-y4)/float(y1-y4)+x4 , (x3-x2)*(y-y2)/float(y3-y2)+x2)
        #print x,y,minx,maxx,miny,maxy
        if minx<= x <= maxx and miny <= y <= maxy:
            return True
        else:
            return False
for y in xrange(h):
    for x in xrange(w):
        if inSquare(x,y):
            display[y][x]="#"
#output

for y in xrange(h):
    print "".join(display[y])
