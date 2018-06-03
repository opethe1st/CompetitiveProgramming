
def solution(A):
    def countGreater(A, a):
        count = 0
        for i in range(a - 1):
            if A[i] > A[a]:
                count += 1
        return count

    dp = [0] * len(A)
    dp[0] = 1
    for i in range(1, len(A)):
        dp[i] = countGreater(A, i) + dp[i - 1] + 1
    return sum(dp)


print(solution([4, 6, 2, 1, 5]))
