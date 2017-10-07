#!/bin/python

import sys


n = int(raw_input().strip())

def minstr(n):
    if n==2:
        return "min(int, int)"
    else:
        return "min(int, "+minstr(n-1)+")"
    
print minstr(n)