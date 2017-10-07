#Week of Code 27 - https://www.hackerrank.com/contests/w27/challenges/drawing-book/copy-from/8192256

"""
if you flip from the first page, you require n/2 flips to get to page n. if you flip from the back, if n is odd, 
you do not need to flip to get to say n-1 but if n is even then you need one flip to get to n-1 and other cases follow.abs
Find the minimum number of flips from the front and from the back and print as answer
"""

#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())
#find the minimum number of pages to flip from the first page, or from the back
print min(p/2,(n-p)/2 if n%2==1 else (n-p+1)/2)