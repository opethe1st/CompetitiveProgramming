def solution(A):
    A.sort()
    for i in xrange(len(A)-2):
        if A[i]+A[i+1] > A[i+2]:
            return 1
    else:
        return 0
