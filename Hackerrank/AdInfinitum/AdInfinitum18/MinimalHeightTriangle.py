#!/bin/python

import sys
from math import ceil


def lowestTriangle(base, area):
    # Complete this function
    return int(ceil(area / float(base) * 2))


base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
