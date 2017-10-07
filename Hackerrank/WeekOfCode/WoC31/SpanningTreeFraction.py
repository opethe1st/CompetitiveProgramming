
parent = dict()
rank = dict()

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
EDGES = {}
for a0 in xrange(m):
    u,v,a,b = raw_input().strip().split(' ')
    u,v,a,b = [int(u),int(v),int(a),int(b)]
    # Write Your Code Here
    EDGES[(u,v)]=(a,b)
    EDGES[(v,u)]=(a,b)

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def compare(a,b):
    m,n=EDGES[a]
    x,y=EDGES[b]
    value = m*y-x*n
    if value>0:
        return 1
    elif value==0:
        return 0
    else:
        return -1

def kruskal(graph):
    for vertice in xrange(n):
        make_set(vertice)

    #minimum_spanning_tree = set()
    edges = EDGES.keys()
    edges.sort(cmp=compare)
    res = 0,0
    for edge in edges:
        vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            #minimum_spanning_tree.add(edge)
            a,b =res
            res = a+vertice1,b+vertice2
    return res



print solve(range(n),n)
