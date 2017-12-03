'''https://www.hackerrank.com/contests/w35/challenges/triple-recursion'''

n, m, k = list(map(int, input().split()))  # pylint: disable=C0103

arr = [[0 for i in range(n)] for j in range(n)] # pylint: disable=C0103
for i in range(n):
    arr[i][i] = m + i*k

for i in range(n):
    for j in range(n):
        if i > j:
            arr[i][j] = arr[j][j] -(i-j)
        elif i < j:
            arr[i][j] = arr[i][i] -(j-i)

for i in range(n):
    print(" ".join(list(map(str, arr[i]))))