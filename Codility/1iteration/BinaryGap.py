import math
import time


start = time.time()


def longestGap(n):
    maxgap = 0  # Initially the max gap is zero
    gap = 0  # stores the current gap length
    while n & 1 == 0:
        n >>= 1  # removes a bit. We could have used n>>1 for this.
    # print n
    while n & (n - 1):  # while the number is greater than zero
        if n & 1:  # check if the number is odd. We could have used n&1
            if gap > maxgap:  # if we got a one, then we need to check if the length of the last gap was greater than the current maxgap
                maxgap = gap  # new maxgap
            gap = 0  # set the current gap length to 0
        else:
            gap += 1  # if n&1 is 0 then a zero was the last bit and the adds to the length of the maxgap
        n >>= 1  # remove the last bit. We could use n>>1 for this too
    return maxgap


def binaryGap(N):
    if N == 0:
        return 0
    maxGap = 0
    prevBit = int(math.log(N & -N, 2)) + 1
    N = N & (N - 1)

    while N != 0:
        newBit = int(math.log(N & -N, 2)) + 1
        maxGap = max(newBit - prevBit - 1, maxGap)

        currBit = newBit
        N = N & (N - 1)

    return maxGap


for i in xrange(10):
    for num in inps:
        longestGap(num)
print time.time() - start
