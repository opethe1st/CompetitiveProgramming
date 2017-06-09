def solution(A):
    minIndex = 0
    minVal = (A[0] + A[1])/2.0
    for i in xrange(len(A)-1):
        if minVal > (A[i]+A[i+1])/2.0:
            minVal = (A[i]+A[i+1])/2.0
            minIndex = i
    for i in xrange(len(A)-2):
        if minVal > (A[i]+A[i+1]+A[i+2])/3.0:
            minVal = (A[i]+A[i+1]+A[i+2])/3.0
            minIndex = i
        elif minVal == (A[i]+A[i+1]+A[i+2])/3.0:
            if minIndex > i:
                minIndex = i
    return minIndex