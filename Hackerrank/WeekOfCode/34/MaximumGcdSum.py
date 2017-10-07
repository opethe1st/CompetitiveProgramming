"""
Maximum possible gcd is 10^6. 
check all the factors of A[i] greater than sqrt(A[i])
"""
from fractions import gcd
import time

start = time.time()
def maximumGcdAndSum(A, B):
    #maximum possible value of a in A or b in B   +1
    R = max(max(A)+1, max(B)+1)
    
    #Array to mark which values exist in A or B
    countA = [0]*(R)
    countB = [0]*(R)
    for a in A:
        countA[a] |= 1
    for b in B:
        countB[b] |= 1
    #print countA
    #print countB
    ans = 0
    maxgcd = 0
    maxgcdsum = 0
    for i in xrange(1, R):
        #i is a potential gcd, j is a multiple of i
        k = 0
        l = 0
        for j in xrange(i, R, i):
            k |= countA[j]
            l |= countB[j]
        if l+k >= 2:
            maxgcd = i
    assert maxgcd >= 1
    maxa, maxb = 0,0
    for a in A:
        if a%maxgcd == 0:
            maxa = max(a, maxa)
    for b in B:
        if b%maxgcd == 0:
            maxb = max(b, maxb)  
    # print maxgcd, maxa, maxb
    return maxa+maxb


if __name__ == "__main__":
    n = int(raw_input().strip())
    A = map(int, raw_input().strip().split(' '))
    B = map(int, raw_input().strip().split(' '))
    res = maximumGcdAndSum(A, B)
    print res
print time.time()-start