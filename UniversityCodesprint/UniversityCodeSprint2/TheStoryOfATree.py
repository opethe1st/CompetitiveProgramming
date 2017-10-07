
G = [set() for i in xrange(n)]

G[u].add(v)
G[v].add(u)

Graph = [set() for i in xrange(n)]
visited=[0]*n
count = 0
def bfs(G,u):
    visited[u]=True
    for v in G[u]:
        if not visited[v]:
            Graph[u].append(v)
            if (u,v) in guesses:
                count+=1
            bfs(G,v)

ans = 0
Graph2 = [Graph[u].copy() for u in xrange(n)]
def bfs2(Graph,u):
    ans += int(count>k)
    for v in Graph2[u]:
        Graph[v].add(u) #reverse
        Graph[u].remove(v) 
        if (u,v) in guesses:
            count-=1
        if (v,u) in guesses:
            count-1
        bfs2(Graph,v)
        Graph[u].add(v) #undo
        Graph[v].remove(u)  

bfs