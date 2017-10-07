#!/bin/python

import sys
sys.setrecursionlimit(10000)
from fractions import gcd
count = 0
ans = 0
def bfs(G,u):
    global count
    global Graph
    visited[u]=True
    #print u
    for v in G[u]:
        if not visited[v]:
            Graph[u].add(v)
            if (u,v) in guesses:
                count+=1
            bfs(G,v)

def bfs2(Graph,u):
    global count
    global ans
    global Graph2
    
    ans += int(count>=k)
    #print 'c',count,'u',u
    for v in Graph2[u]:
        Graph[v].add(u) #reverse
        Graph[u].remove(v) 
        if (u,v) in guesses:
            count-=1
        if (v,u) in guesses:
            count+=1
        bfs2(Graph,v)
        Graph[u].add(v) #undo
        Graph[v].remove(u)
        if (u,v) in guesses:
            count+=1
        if (v,u) in guesses:
            count-=1


q = int(raw_input().strip())
for a0 in xrange(q):
    n = int(raw_input().strip())
    
    G = [set() for i in xrange(n)]
    for a1 in xrange(n-1):
        u,v = raw_input().strip().split(' ')
        u,v = [int(u),int(v)]
        G[u-1].add(v-1)
        G[v-1].add(u-1)
    
    g,k = raw_input().strip().split(' ')
    g,k = [int(g),int(k)]
    guesses = set()
    for a1 in xrange(g):
        u,v = raw_input().strip().split(' ')
        u,v = [int(u),int(v)]
        guesses.add((u-1,v-1))
        
    Graph = [set() for i in xrange(n)]   
    visited=[0]*n
    count = 0
    bfs(G,0)
    #print 'count',count
    
    ans = 0
    Graph2 = [Graph[u].copy() for u in xrange(n)]
    bfs2(Graph,0)
    
    print str(ans/gcd(ans,n))+'/'+str(n/gcd(ans,n))
    