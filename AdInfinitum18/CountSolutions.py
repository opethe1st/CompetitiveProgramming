#!/bin/python

import sys
from math import sqrt


def solve1(a, y, b):
    try:
        return (a + sqrt(a**2 - 4 * (y**2 - b * y))) / 2.0
    except:
        return 0


def solve2(a, y, b):
    try:
        return (a - sqrt(a**2 - 4 * (y**2 - b * y))) / 2.0
    except:
        return 0


def countSolutions(a, b, c, d):
    # Complete this function
    count = 0
    for y in range(1, d + 1):
        x1 = solve1(a, y, b)
        x2 = solve2(a, y, b)
        if int(x1) == x1 and 1 <= x1 <= c:
            count += 1
        if int(x2) == x2 and 1 <= x2 <= c and x1 != x2:
            count += 1
    return count


q = int(raw_input().strip())
for a0 in xrange(q):
    a, b, c, d = raw_input().strip().split(' ')
    a, b, c, d = [int(a), int(b), int(c), int(d)]
    result = countSolutions(a, b, c, d)
    print(result)
