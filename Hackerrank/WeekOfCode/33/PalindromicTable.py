#!/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
sys.setrecursionlimit(1000000)


def palindrome(A, a, b, c, d):
    pal = xorsum[a][b] ^ xorsum[c][d] ^ xorsum[a][d] ^ xorsum[c][b]
    nzero = nzeroes[c][d] - nzeroes[a][d] - nzeroes[c][b] + nzeroes[a][b]
    if (pal & (pal - 1)) == 0 and nzero < (c - a) * (d - b) - 1:
        return True
    else:
        return False


cachePal = {}


def isPalindrome(A, n, m):
    if (n, m) in cachePal:
        return cachePal[(n, m)]
    N = len(A)
    M = len(A[0])
    if n == 1 and m == 1:
        return 0, 0, 0, 0
    for a in range(N - n + 1):
        for b in range(M - m + 1):
            if palindrome(A, a, b, a + n, b + m):
                cachePal[(n, m)] = (a, b, a + n - 1, b + m - 1)
                return a, b, a + n - 1, b + m - 1
    cachePal[(n, m)] = False
    return


cache = {}


def largestBeautiful(A, a, b, n, m):
    """returns the largest beautiful A of size less than or equal to n*m"""
    # print n, m
    if n < 1 or m < 1:
        return ((0, 0, 0, 0), 1)
    if n * len(A[0]) + m in cache:
        return cache[n * len(A[0]) + m]
    if palindrome(A, a, b, a+n, b+m):
        return ((a, b, a+n, b+m), n*m)
    else:
        N = len(A)
        M = len(A[0])
        if n == 1 and m == 1:
            c = 0, 0, 0, 0
        maxval = 1
        for a in range(N - n + 1):
            for b in range(M - m + 1):
                c, d = a+n, b+m
                nzero = nzeroes[c][d] - nzeroes[a][d] - nzeroes[c][b] + nzeroes[a][b]
                if nzero >= (c - a) * (d - b) - 1:
                    palindrome(A, a, b, c, d)
        c = isPalindrome(A, n, m)  # is there a beautiful rect of size n, m
        if c:  # there is a valid coordinate of size n*m
            cache[n * len(A[0]) + m] = (c, n * m)
            return (c, n * m)
        else:
            c1, area1 = largestBeautiful(A, n - 1, m)
            c2, area2 = largestBeautiful(A, n, m - 1)
            if area1 > area2:
                cache[n * len(A[0]) + m] = (c1, area1)
                return c1, area1
            else:
                cache[n * len(A[0]) + m] = (c2, area2)
                return c2, area2


n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

table = []
for table_i in range(n):
    table_temp = (map(int, raw_input().strip().split(' ')))
    table.append(table_temp)
#print (table, type(table))
xorsum = [[0 for j in range(m + 1)] for i in range(n + 1)]
nzeroes = [[0 for j in range(m + 1)] for i in range(n + 1)]
for i in range(1, n + 1):
    xorsum[i][0] = 0
    nzeroes[i][0] = 0
    s = 0
    col = 0
    for j in range(1, m + 1):  # columns
        col = col ^ (1 << table[i - 1][j - 1])
        xorsum[i][j] = xorsum[i - 1][j] ^ (col)
        s += int(table[i - 1][j - 1] == 0)
        # print s,
        nzeroes[i][j] = nzeroes[i - 1][j] + s
if nzeroes[n][m] >= (n * m - 1):
    ans = ((0, 0, 0, 0), 1)
    ans = largestBeautiful(table, n, m)
    print (ans[1])
    print ('%d %d %d %d ' % ans[0])
else:
    ans = largestBeautiful(table, n, m)
    print (ans[1])
    print ('%d %d %d %d ' % ans[0])
