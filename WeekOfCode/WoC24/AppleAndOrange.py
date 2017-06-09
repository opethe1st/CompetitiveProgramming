"""Hackerrank Week Of Code 24. Problem Description - https://www.hackerrank.com/contests/w24/challenges/apple-and-orange/copy-from/7306771"""

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))
print len([a+d for d in apple if s<=a+d<=t])
print len([b+d for d in orange if s<=b+d<=t])