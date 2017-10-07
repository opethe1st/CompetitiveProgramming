#!/bin/python
# https://www.hackerrank.com/contests/world-codesprint-9/challenges/weighted-uniform-string
import sys

s = raw_input().strip()
charArray = [0]*26
prev = s[0]
count = 0
for letter in s[1:]:
    count+=1
    if prev!=letter:
        charArray[ord(prev)-ord('a')]=max(charArray[ord(prev)-ord('a')],count)
        count=0
    prev = letter
else:
    count+=1
    charArray[ord(prev)-ord('a')]=max(charArray[ord(prev)-ord('a')],count) #this is for the last letter
#print charArray
n = int(raw_input().strip())
for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    for i in xrange(26):
        if 0<x/(i+1)<=charArray[i]:
            if x%(i+1)==0:
                print "Yes"
                break
    else:
        print "No"
    
