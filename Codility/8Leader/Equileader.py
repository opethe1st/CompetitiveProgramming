def findDominator(A):
    # write your code in Python 2.7
    if A == []:
        return -1
    B = A[:]
    B.sort()
    #print A.count(A[len(A)/2])
    if A.count(B[len(A)/2]) > len(A)/2:
        return B[len(A)/2]
    else:
        return -1


def solution(A):
    dom = findDominator(A)
    if dom == -1:
        return 0
    else:
        countdom = 0
        countdomback = A.count(dom)
        ans = 0 
        for i in xrange(len(A)):
            if A[i] == dom:
                countdom += 1
                countdomback -= 1
            #print countdom,countdomback
            if 2*countdom > (i+1) and 2*countdomback>(len(A)-i-1):
                ans += 1
        return ans