def solution(A):
    # write your code in Python 2.7
    if A == []:
        return -1
    B = A[:]
    B.sort()
    #print A.count(A[len(A)/2])
    if A.count(B[len(A)/2]) > len(A)/2:
        return A.index(B[len(A)/2])
    else:
        return -1