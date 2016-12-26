#Week of Code 27 - https://www.hackerrank.com/contests/w27/challenges/coprime-paths
"""This wasn't good enough to pass all the testcases. 
The basic idea is to have a dfs that finds all paths from a given start to every other node and calculates the number 
of nodes coprime to start value on the path to a given node. This is stored in s[node]
To calculate the actual value, we find the path from u to v and then sum s[i][u] where u is  the start and i is a node
on the path from u to v with v included
"""

import sys
from fractions import gcd

n,q = raw_input().strip().split(' ')
n,q = [int(n),int(q)]
nodes = map(int,raw_input().strip().split(' '))
#Build the Graph
G = [[] for i in xrange(n)]
for _ in xrange(n-1):
    u,v = map(int,raw_input().strip().split(' '))
    G[u-1].append(v-1)
    G[v-1].append(u-1)

#All co-prime pairs 
coprime = [[0 for i in xrange(n)] for j in xrange(n)]
for u in xrange(n):
    for v in xrange(n):
        if gcd(nodes[u],nodes[v])==1:
            coprime[u][v]=1
            coprime[v][u]=1

#find path from start to every other node, find ns which is the number of nodes coprime with start on the path from start to v
def dfs(start,u):
    visited[u]=True
    global G
    for v in G[u]:
        if not visited[v]:
            ns[v]=ns[u]+coprime[start][v]
            prev[v]=u
            dfs(start,v)

s = [[0 for i in xrange(n)] for j in xrange(n)]
p = [[0 for i in xrange(n)] for j in xrange(n)]

#store all the s values and all the paths
for node in xrange(n):
    ns = [0 for i in xrange(n)]
    prev = [float("inf") for i in xrange(n)]
    #prev[node]=node
    visited=[False]*n
    dfs(node,node)
    #print ns
    s[node]=ns
    p[node]=prev

for a0 in xrange(q):
    #remember to substract one before I used u or v
    u,v = map(int,raw_input().split())
    # your code goes here
    #print u,v
    u=u-1
    v=v-1
    prev = p[u]
    #print prev
    noCoPrime=0
    while v!=float('inf'):
        noCoPrime+=s[v][u]
        #print u,v,s[v][u]
        v = prev[v]
    print noCoPrime
