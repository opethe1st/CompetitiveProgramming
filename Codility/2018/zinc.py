
def solution(A):
    MODULO = 1000000007
    N = len(A)
    if len(A) < 3:
        return 0
    dp = [[0 for i in range(N+1)] for i in range(4)]
    M = set()
    for n in range(1, N+1):
        M.add(A[n-1])
        dp[1][n] = len(M)
    for k in range(2, 4):
        dp[k][k] = 1
        count_k_group_end_with_num_dict = {}
        count_k_group_end_with_num_dict[A[k-1]] = 1
        for n in range(k+1, N+1):
            w = dp[k-1][n-1] - count_k_group_end_with_num_dict.get(A[n-1], 0)
            dp[k][n] = (dp[k][n-1] + w)%MODULO
            count_k_group_end_with_num_dict[A[n-1]] = (count_k_group_end_with_num_dict.get(A[n-1], 0) + w)%MODULO
    return dp[3][N]
                                                                                                
print(solution(A=list(range(1, 100000))))
