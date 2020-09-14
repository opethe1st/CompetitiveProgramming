"""
Link to (question)[https://www.codechef.com/SEPT20B/problems/ADAMAT]
The key insight is that when a row or column is out of order, we want to sort
it using the smallest number of operations. To do this, we could iterate from
the largest submatrix to the smallest one and rotate whenever a given
submatrix is out of order. Since the matrix will out of order n times, then
it will be transposed at most n times. (it is possible it is less than n since
one transpose operation might fix two out of order rows or columns).
This is a greedy algorithm.
"""


def is_sorted_submatrix(matrix, size, n):
    i = size - 1
    for j in range(size):
        if (n * i + j + 1) != matrix[i][j]:
            return False
    j = size - 1
    for i in range(size):
        if (n * i + j + 1) != matrix[i][j]:
            return False
    return True


def transpose(matrix, size):
    for i in range(size):
        for j in range(i, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def solution(matrix, n):
    count = 0
    for size in range(n, -1, -1):
        if not is_sorted_submatrix(matrix, size, n):
            transpose(matrix, size)
            count += 1
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    print(solution(matrix, N))
