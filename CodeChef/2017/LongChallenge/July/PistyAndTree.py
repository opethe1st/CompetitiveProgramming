# Not solved yet.
def buildTree(G):
    """returns the dfs tree and an array with the level of each node in 
    the dfs tree """
    visited = [False] * len(G)
    parent = [-1] * len(G)
    parent[0] = 0  # the root of the tree
    level = [-1] * len(G)
    stack = [0]
    while stack:
        u = stack.pop(-1)
        level[u] = level[parent[u]] + 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                stack.append(v)
                parent[v] = u
    parent[0] = -1
    return parent, level


print buildTree([[1, 2], [0, 3, 4], [0, 4, 7, 8], [1, 5, 6], [1, 2], [], [], [], []])


def preprocess(Parent, W, C):
    n = len(Parent)
    logn = 0
    while n > 0:
        logn += 1
        n >>= 1
    # assert ((logn+1)+1 == len(bin(n)))
    P = [[-1 for i in xrange(logn)] for j in xrange(n)]
    A = [[-1 for i in xrange(logn)] for j in xrange(n)]
    P[0][0] = Parent[i]
    for i in xrange(1, n):
        P[i][0] = Parent[i]
        if W[(i, Parent[i])] <= C:
            A[i][0] = W[(i, Parent[i])]
        else:
            A[i][0] = 0

    j = 1
    while ((1 << j) < n):
        for i in xrange(n):
            if (P[i][j - 1] != -1):  # if the root has been reached
                P[i][j] = P[P[i][j - 1]][j - 1]
                A[i][j] = A[i][j - 1] ^ A[P[i][j - 1]][j - 1]
        j += 1
    return P, A


# print preprocess(range(2))
def totalAttractivity(G, W, u, v, C):
    parent, level = buildTree(G)
    P, A = preprocess(Parent, W, C)
    p, q = u, v
    if L[p] < L[q]:
        p, q = q, p
    logn = 0
    while n > 0:
        logn += 1
        n >>= 1
    ans = 0
    i = logn
    while i >= 0:
        if (L[p] - (1 << i) >= L[q]):
            p = P[p][i]
            ans ^= A[p][i]
        i -= 1

    if (p == q):
        return p

    i = logn
    while i >= 0:
        if (P[p][i] != -1 and P[p][i] != P[q][i]):
            p = P[p][i]
            q = P[q][i]
            ans ^= A[p][i]
            ans ^= A[q][i]
        i -= 1
        if P[p][i] == P[q][i]:
            ans ^= A[p][i]
            ans ^= A[q][i]
            break
    # return Parent[p]
    return ans


T = input()
for _ in xrange(T):
    N = input()
    G = [[] for i in xrange(N)]
    W = {}
    for i in xrange(N):
        u, v, w = map(int, raw_input().split())
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
        W[(u - 1, v - 1)] = w
        W[(v - 1, u - 1)] = w
    M = input()
    

