import sys


def dfs(G, n):
    global clock
    visited = [False] * (n)
    pre = [-1] * (n + 1)
    post = [-1] * (n + 1)
    order = []
    clock = 0

    def dfsVisit(G, u):
        global clock
        pre[u] = clock
        clock += 1
        visited[u] = True
        # print num2letter[u],
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v)
        post[u] = clock
        order.append(u)
        clock += 1

    for node in xrange(1, n):
        if not visited[node]:
            dfsVisit(G, node)
    return order


def getSCC(G, n):
    component = [0] * (n)

    def dfsVisit(G, u, c):
        visited[u] = True
        component[u] = c
        s.add(u)
        for v in G[u]:
            if not visited[v]:
                dfsVisit(G, v, c)
    order = dfs(G, n)
    visited = [False] * (n)
    c = 0
    for node in order:
        if not visited[node]:
            s = set()
            c += 1
            dfsVisit(G, node, c)
            # print s
    return component


def transform(a, n, transformations):
    # run strongly connected component algo
    # print transformations
    comp = getSCC(transformations, n)
    # print comp
    for j in xrange(len(a)):
        a[j] = comp[a[j]]
    return a


def longestPalin2(s):
    dp = [[0 for i in xrange(len(s))] for j in xrange(len(s))]
    for i in xrange(len(s)):
        dp[i][i] = 1
    for d in xrange(1, len(s)):
        for start in xrange(len(s) - d):
            # print d,start
            if s[start] == s[start + d] and d == 1:
                dp[start][start + d] = 2
            elif s[start] == s[start + d] and d != 1:
                dp[start][start + d] = dp[start + 1][start + d - 1] + 2
            else:
                val2 = dp[start + 1][start + d]
                val3 = dp[start][start + d - 1]
                dp[start][start + d] = max(val2, val3)
    return dp[0][len(s) - 1]


# input
n, k, m = raw_input().strip().split(' ')
n, k, m = [int(n), int(k), int(m)]
transformations = [[] for i in xrange(n)]
for a0 in xrange(k):
    x, y = raw_input().strip().split(' ')
    x, y = [int(x), int(y)]
    transformations[x - 1].append(y - 1)
    transformations[y - 1].append(x - 1)
    # transformations.reverse()
a = map(int, raw_input().strip().split(' '))
a = [val - 1 for val in a]
print longestPalin2(transform(a, n, transformations))
