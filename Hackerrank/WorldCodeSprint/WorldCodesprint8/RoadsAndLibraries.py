#!/bin/python
#World Codesprint - https://www.hackerrank.com/contests/world-codesprint-8/challenges/torque-and-development
import sys

#Depth First Search. Find all the nodes reachable from the start vertex
def dfs(node):
    start=node
    for v in G[start]:
        if not visited[v]:
            visited[v]=True
            dfs(v)


q = int(raw_input().strip())
for a0 in xrange(q):
    n,m,x,y = raw_input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    
    G = [[] for i in xrange(1+n)]
    for a1 in xrange(m):
        city_1,city_2 = raw_input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        G[city_1].append(city_2)
        G[city_2].append(city_1)
    visited=[False]*(n+1)
    #count the number of clusters
    nclusters = 0
    for node in xrange(1,n+1):
        if not visited[node]:
            dfs(node)
            nclusters+=1
    #print nclusters
    #if cost of building a lib, x is less then cost of repairing road,y then  build nlibraries else build 
    #just a library in each cluster and repair the roads
    if x>y:
        print nclusters*x+(n-nclusters)*y
    else:
        print n*x
