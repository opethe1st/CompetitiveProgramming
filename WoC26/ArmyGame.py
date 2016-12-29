#!/bin/python
# Week of Code 26 - https://www.hackerrank.com/contests/w26/challenges/game-with-cells
import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]

print (int(m/2.0+0.5)*int(n/2.0+0.5))