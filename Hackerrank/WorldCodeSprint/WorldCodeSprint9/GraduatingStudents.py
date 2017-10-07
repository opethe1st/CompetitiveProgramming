#Question description https://www.hackerrank.com/contests/world-codesprint-9/challenges/grading
import sys

n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    # your code goes here
    nextMultiple5 = (grade/5)*5+5
    if grade<38:
        print grade
    elif nextMultiple5-grade<3:
        print nextMultiple5
    else:
        print grade
