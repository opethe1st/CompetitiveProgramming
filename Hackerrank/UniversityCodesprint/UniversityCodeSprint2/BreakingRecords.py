#!/bin/python

import sys


n = int(raw_input().strip())
scores = map(int, raw_input().strip().split(' '))
# your code goes here
mini = scores[0]
maxi = scores[0]
countBestRecords = 0
countWorstRecords = 0
for score in scores:
    if score>maxi:
        maxi = score
        countBestRecords+=1
    elif score<mini:
        mini = score
        countWorstRecords+=1
        
print countBestRecords,countWorstRecords