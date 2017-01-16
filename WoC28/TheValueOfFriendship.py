import time
countnodes=0
def dfs(node):
    global G
    global countnodes
    stack = [node]
    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex]=True
            countnodes+=1
            for v in G[vertex]:
                stack.append(v)


start = time.time()
def valuefriendship(n):
    return n*(2*n-1)*(n-1)/6+(n)*(n-1)/2

t = int(raw_input().strip())
for a0 in xrange(t):
    n,m = raw_input().strip().split(' ')
    n,m = [int(n),int(m)]
    G = [[] for i in xrange(n)]
    for a1 in xrange(m):
        x,y = raw_input().strip().split(' ')
        x,y = [int(x),int(y)]
        G[x-1].append(y-1)
        G[y-1].append(x-1)       
    
    visited=[False]*(n+1)
    #count the number of clusters
    total = 0
    ncomponents = 0
    components = []
    for node in xrange(n):
        if not visited[node]:
            ncomponents+=1
            countnodes = 0
            dfs(node)
            components.append(countnodes)

    components.sort()
    #print components,ncomponents
    for i in xrange(ncomponents):
        total+=valuefriendship(components[i])
        #print total
    #print total
    prefixs = [0]*(len(components)+1)
    for i in xrange(len(components)):
        prefixs[i+1]=prefixs[i]+components[i]-1
    #print total,prefixs
    for i in xrange(len(components)):
        #print prefixs[i],(components[i]-1)*(components[i])
        total+=prefixs[i]*(components[i]-1)*(components[i])
    total+=(m-n+ncomponents)*sum([v*(v-1) for v in components])
    print total

print time.time()-start