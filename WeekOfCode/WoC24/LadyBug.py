""" Week of Code 24 - https://www.hackerrank.com/contests/w24/challenges/happy-ladybugs"""

import sys
#!/bin/python

import sys
def ladyBugHappy(s):
    """test if in a board with no spaces, all ladybugs are happy """
    if len(s)==1:
        return "NO"
    prev = s[0]
    count=1
    for i in xrange(1,len(s)):
        if prev!=s[i]:
            if count==1:
                return "NO"
            count=0
        prev =s[i]
        count+=1
    return "YES"

def canLadyBugHappy(s):
    """Returns "YES" if all lady bugs can be made happy. Return "NO" if there is a ladybug that is not happy """
    characters ={}
    for l in s:
        characters[l]=characters.get(l,0)+1
    #I didnt have to use a hashmap though... an array with A-Z would have been enough
    for l in characters:
        if l!='_':
            if characters[l]==1:
                return "NO"
    if characters.get('_',0)>0:
        return "YES"
    else:
        return ladyBugHappy(s)

Q = int(raw_input().strip())
for a0 in xrange(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    print canLadyBugHappy(b)
