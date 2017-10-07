#!/bin/python

import sys


def towerColoring(n):
    # Complete this function
    raiseTo = pow(3, n, 1000000006)
    return pow(3, raiseTo, 1000000007)


n = int(raw_input().strip())
result = towerColoring(n)
print(result)
