import sys
sys.setrecursionlimit = 100000

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]

sources = set(range(n))
G = [[] for i in xrange(n)]
for a0 in xrange(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    G[u - 1].append(v - 1)
    if v - 1 in sources:
        sources.remove(v - 1)

prev = [-1] * n
post = [-1] * n
visited = [False] * n
clock = 0

# Are there cycles????
head = range(50000)
tail = range(50000)

def dfs(G, u):
    # print u,clock
    global clock
    visited[u] = True
    prev[u] = clock
    clock += 1
    for v in G[u]:
        if not visited[v]:
            dfs(G, v)
        else:
            head[v] = head[u]
    post[u] = clock
    # print 'post',u,clock
    clock += 1

#print sources
for node in xrange(n):
    if not visited[node]:
        dfs(G, node)
print prev
print post


def connectNode(d, x, n):
    if d == 0:
        head[n] = head[x]
    else:
        tail[n] = tail[x]

    n += 1
    return n


def check(x, y):
    if x == y:
        return True
    if head[x] == head[y]:
        print 'here'
        if x < y:
            return True
        else:
            return False
    elif tail[x] == tail[y]:
        if y > x:
            return True
        else:
            return False
    else:
        x = tail[x]
        y = head[y]
        print x, y, prev[x], post[x], prev[y], post[y]
        print head[:10]
        print tail[:10]
        if x < ncopy and y < ncopy:
            if prev[x] <= prev[y] <= post[y] <= post[x]:
                return True
            else:
                return False
        else:
            return False


ncopy = n
q = int(raw_input().strip())
for a0 in xrange(q):
    op, x, y = raw_input().strip().split(' ')
    op, x, y = [int(op), int(x), int(y)]
    if op == 1:
        n = connectNode(y, x - 1, n)
    else:
        if check(x - 1, y - 1):
            print "Yes"
        else:
            print 'No'
