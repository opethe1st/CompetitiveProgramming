"""
Matrix with N rows and N columns. containing all integers from 1 to N**2
Ada wants to sort the matrix in row-major order.
for each valid i and j, she wants the cell (i, j) to contain the value
(i-1)*N +j
In one operation, Ada should choose an integer L and transpose the submatrix
between rows 1 and L and the columns 1 and L inclusive.
Find the smallest number of operations needed to sort the matrix
Focus on the values at the each other edge
and from behind. So the challenge is to make it in the right order.
Ideas
Idea
Go through L from right to left.
if any of the values at the edges is wrong, then make a swap.
Actually do the transpose? Can focus on just the edges.
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]

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
            # print('pre-transpose ', matrix)
            transpose(matrix, size)
            # print('post-transpose', matrix)
            # print()
            count += 1
    return count


T = int(input())
for _ in range(T):
    N = int(input())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))

    print(solution(matrix, N))
