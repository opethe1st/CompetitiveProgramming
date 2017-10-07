def solution(A):
    mini = A[0]
    minindex = 0
    for i in xrange(len(A)):
        if mini > A[i]:
            mini = A[i]
            minindex = i
    return minindex+1

T = input()

for _ in xrange(T):
    N = input()
    A = map(int, raw_input().split())
    print(solution(A))