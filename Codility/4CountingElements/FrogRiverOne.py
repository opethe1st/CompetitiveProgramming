def solution(X, A):
    leavesPosition = [0] * (X+1)
    count = 0
    for i in range(len(A)):
        if A[i]-1 <= X:  # count the number of leaves at positions<X
            if leavesPosition[A[i] - 1] == 0:  # no leaves at this position
                count += 1
                leavesPosition[A[i] - 1] = 1  # leaf at this position
        if count == X:
            return i
        #  print count
    return -1
A = [0]*8
A[0] = 1
A[1] = 3
A[2] = 1
A[3] = 4
A[4] = 2
A[5] = 3
A[6] = 5
A[7] = 4

print solution(5, A)
