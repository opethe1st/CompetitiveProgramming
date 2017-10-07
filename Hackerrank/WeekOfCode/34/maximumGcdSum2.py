
def maximumGcdSum(A, B):
    countA = [0]*(max(A)+1)
    countB = [0]*(max(B)+1)
    for a in A:
        countA[a] |= 1
    for b in A:
        countB[b] |= 1
    ans = 0
    for i in xrange(1, max(A)+1):
        k = 0
        for j in xrange(i, n, i):
            k += countA[j]
            k += countB[j]
        if k >= 2:
            ans = max(ans, i)
    return ans
