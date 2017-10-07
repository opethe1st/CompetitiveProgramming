#!/bin/python

import sys


def pythagoreanTriple(a):
    # Complete this function
    if a % 2 == 1:
        # a has to be of the form m^2-n^2.. any possible answer!
        k = a / 2
        return (a, 2 * k * (k + 1), (k + 1)**2 + k**2)
    else:
        # a is of the form m^2-n^2 or 2mn.. find all possible m and n
        mn = a / 2
        n = 1
        m = mn
        return (m**2 - n**2, 2 * m * n, m**2 + n**2)


a = int(raw_input().strip())
triple = pythagoreanTriple(a)
print " ".join(map(str, triple))
